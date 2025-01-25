import json
import logging

from dataclasses import dataclass, field
from asyncio import Queue
from uuid import uuid4


from almabtrieb.util import parse_connection_string

from .base import MqttBaseConnection

logger = logging.getLogger(__name__)


@dataclass
class MqttConnection:
    echo: bool
    username: str
    base_connection: MqttBaseConnection

    incoming_queue: Queue = field(default_factory=Queue)
    outgoing_queue: Queue = field(default_factory=Queue)

    result_queues: dict[str, Queue] = field(default_factory=dict)

    @staticmethod
    def from_connection_string(
        connection_string: str, echo: bool = False
    ) -> "MqttConnection":
        parsed = parse_connection_string(connection_string)
        return MqttConnection(
            base_connection=MqttBaseConnection(**parsed, echo=echo),
            echo=echo,
            username=parsed["username"],
        )

    @property
    def connected(self):
        return self.base_connection.connected

    @property
    def receive(self):
        return f"receive/{self.username}/#"

    @property
    def send_topic(self):
        return f"send/{self.username}"

    async def run(self):
        async with self.base_connection.run([self.receive]) as client:
            async for message in client.messages:
                data = json.loads(message.payload)
                correlation_id = getattr(message.properties, "CorrelationData").decode()
                if self.echo:
                    logger.info(
                        "%s %s %s",
                        str(message.topic),
                        correlation_id,
                        json.dumps(data, indent=2),
                    )

                if message.topic.matches("receive/+/response/+"):
                    await self.result_queues[correlation_id].put(data)
                else:
                    await self.incoming_queue.put

    async def send(
        self, topic_end: str, data: dict, correlation_data: str | None = None
    ) -> bytes:
        topic = f"{self.send_topic}/{topic_end}"

        correlation_data = await self.base_connection.send(
            topic, data, correlation_data=correlation_data
        )

        return correlation_data

    async def send_with_reply(self, topic_end: str, data: dict):
        correlation_id = str(uuid4())

        self.result_queues[correlation_id] = Queue()

        await self.send(topic_end, data, correlation_data=correlation_id)

        result = await self.result_queues[correlation_id].get()
        del self.result_queues[correlation_id]

        return result
