from uuid import uuid4
from asyncio import Queue

import json
import logging
import re


logger = logging.getLogger(__name__)

response_regex = re.compile(r"^receive.\w+\.response\.\w+$")
incoming_regex = re.compile(r"^receive.\w+\.incoming$")

try:
    import aio_pika

    class AmqpConnection:
        def __init__(self, connection_string: str, username: str, echo: bool = False):
            self.connection_string = connection_string
            self.echo = echo
            self.channel = None
            self.result_queues = {}
            self.username = username

            self.incoming_queue = Queue()

        @property
        def connected(self):
            return self.channel is not None

        @property
        def subscription_topic(self):
            return f"receive.{self.username}.#"

        def routing_key(self, topic_end: str):
            """
            ```pycon
            >>> connection = AmqpConnection("amqp://guest:guest@localhost/", "alice")
            >>> connection.routing_key("example.one")
            'send.alice.example.one'

            >>> connection.routing_key("example/two")
            'send.alice.example.two'

            ```
            """

            return f"send.{self.username}.{topic_end.replace('/', '.')}"

        async def run(self):
            logger.info("Conneting to amqp with %s", self.connection_string)
            connection = await aio_pika.connect_robust(self.connection_string)

            async with connection:
                self.channel = await connection.channel()
                await self.channel.set_qos(prefetch_count=1)
                self.exchange = await self.channel.declare_exchange(
                    "amq.topic",
                    aio_pika.ExchangeType.TOPIC,
                    durable=True,
                )

                queue = await self.channel.declare_queue(
                    "task_queue_" + str(uuid4()),
                    durable=False,
                )

                await queue.bind(self.exchange, routing_key=self.subscription_topic)

                async with queue.iterator() as iterator:
                    async for message in iterator:
                        async with message.process():
                            await self.handle_message(message)

        async def handle_message(self, message):
            correlation_id = message.correlation_id
            routing_key = message.routing_key
            data = json.loads(message.body)

            if self.echo:
                logger.info(
                    "%s %s %s",
                    routing_key,
                    correlation_id,
                    json.dumps(data, indent=2),
                )

            if response_regex.match(routing_key):
                if correlation_id in self.result_queues:
                    await self.result_queues[correlation_id].put(data)
            elif incoming_regex.match(routing_key):
                await self.incoming_queue.put(data)
            else:
                logger.info("Unknown routing key %s", routing_key)

        async def send(
            self, topic_end: str, data: dict, correlation_data: str | None = None
        ):
            await self.exchange.publish(
                aio_pika.Message(
                    body=json.dumps(data).encode(),
                    correlation_id=correlation_data,
                ),
                routing_key=self.routing_key(topic_end),
            )

            if self.echo:
                logger.info(
                    "Sent %s %s",
                    self.routing_key(topic_end),
                    json.dumps(data, indent=2),
                )

        async def send_with_reply(self, topic_end: str, data: dict):
            correlation_id = str(uuid4())

            self.result_queues[correlation_id] = Queue()

            await self.send(topic_end, data, correlation_data=correlation_id)

            result = await self.result_queues[correlation_id].get()
            del self.result_queues[correlation_id]

            return result

except ImportError:

    class AmqpConnection:
        def __init__(self, *args, **kwargs):
            raise ImportError("aio_pika is not installed")
