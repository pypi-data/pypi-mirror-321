import asyncio
import logging

from dataclasses import dataclass

from .amqp import AmqpConnection
from .mqtt import MqttConnection
from .model import (
    InformationResponse,
    CreateActorRequest,
    FetchMessage,
    FetchResponse,
    TriggerMessage,
)

from .util import ConnectionParams


class NoIncomingException(Exception):
    """Thrown when no incoming message is available"""

    pass


logger = logging.getLogger(__name__)


@dataclass
class Almabtrieb:
    """Implements the asynchronous API of the Cattle Drive Protocol

    :params connection:
    """

    connection: MqttConnection | AmqpConnection

    @property
    def connected(self):
        """Is one connected to the service"""
        return self.connection.connected

    @staticmethod
    def from_connection_string(connection_string: str, echo: bool = False):
        """Creates instance for connection string

        ```pycon
        >>> a = Almabtrieb.from_connection_string("ws://user:pass@host/ws")
        >>> isinstance(a.connection, MqttConnection)
        True

        >>> a = Almabtrieb.from_connection_string("amqp://user:pass@host/ws")
        >>> isinstance(a.connection, AmqpConnection)
        True

        ```

        :param connection_string: The connection string
        :param echo: Set to true to log all messages
        """

        params = ConnectionParams.from_string(connection_string)

        if params.protocol in ["ws", "wss"]:
            return Almabtrieb(
                connection=MqttConnection.from_connection_string(
                    connection_string, echo=echo
                )
            )

        elif params.protocol == "amqp":
            return Almabtrieb(
                connection=AmqpConnection(
                    connection_string=connection_string,
                    echo=echo,
                    username=params.username,
                )
            )
        else:
            raise NotImplementedError("Protocol not implemented")

    async def run(self):
        """Starts the connection and queries for new received messages

        ```python
        task = asyncio.create_task(almabtrieb.run())
        ...
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass
        ```
        """
        await self.connection.run()

    async def info(self) -> InformationResponse:
        """Returns the information about the connected
        Cattle Drive server

        :returns: The information about the server
        """
        result = await self.connection.send_with_reply("request/info", {})

        return InformationResponse.model_validate(result)

    async def create_actor(
        self,
        base_url: str,
        preferred_username: str | None = None,
        profile: dict = {},
        automatically_accept_followers: bool | None = None,
    ) -> dict:
        """Creates a new actor

        :param base_url: The base url of the actor
        :param preferred_username: The preferred username used as `acct:preferred_username@domain` where `domain` is from `base_url`
        :param profile: The profile of the actor
        :param automatically_accept_followers: If true, the server will automatically accept followers
        :returns: The created actor profile
        """
        request = CreateActorRequest(
            base_url=base_url,
            preferred_username=preferred_username,
            profile=profile,
            automatically_accept_followers=automatically_accept_followers,
        )

        return await self.connection.send_with_reply(
            "request/create_actor", request.model_dump()
        )

    async def fetch(self, actor: str, uri: str, timeout: float = 1) -> FetchResponse:
        """Fetches the object with uri `uri` as the actor with actor id `actor`.

        :param actor: The actor id must be part of actors from the info response
        :param uri: The uri of the object to fetch
        :param timeout: The timeout for the request
        :returns: The fetched object
        """
        async with asyncio.timeout(timeout):
            result = await self.connection.send_with_reply(
                "request/fetch", FetchMessage(actor=actor, uri=uri).model_dump()
            )

            return FetchResponse.model_validate(result)

    async def trigger(self, actor: str, method: str, data: dict):
        end = "trigger"
        if method and len(method) > 0:
            end = f"{end}/{method}"
        return await self.connection.send(
            end,
            TriggerMessage(actor=actor, method=method, data=data).model_dump(),
        )

    async def incoming(self):
        """Generator for the incoming messages"""
        while msg := await self.connection.incoming_queue.get():
            yield msg

    async def next_incoming(self, timeout: float = 1) -> dict:
        """Returns the next incoming message

        :param timeout: The timeout for the request
        :returns: The next incoming message
        """
        try:
            async with asyncio.timeout(timeout):
                logger.info("Getting from incoming queue")
                return await self.connection.incoming_queue.get()
        except asyncio.TimeoutError:
            raise NoIncomingException("No incoming message")

    async def clear_incoming(self) -> None:
        """Empties the incoming message queue"""
        while not self.connection.incoming_queue.empty():
            await self.connection.incoming_queue.get()
