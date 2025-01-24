import asyncio
import logging
import ssl
from contextlib import suppress
from http import HTTPStatus
from typing import Awaitable
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Union

from aiohttp import ClientSession, TCPConnector
from aiohttp import ClientTimeout
from aiohttp import ServerConnectionError
from websockets.client import WebSocketClientProtocol
from websockets.client import connect
from websockets.connection import State
from websockets.exceptions import ConnectionClosed

import pysignalr.exceptions as exceptions
from pysignalr import NegotiationTimeout
from pysignalr.messages import CompletionMessage
from pysignalr.messages import Message
from pysignalr.messages import PingMessage
from pysignalr.protocol.abstract import Protocol
from pysignalr.transport.abstract import ConnectionState
from pysignalr.transport.abstract import Transport
from pysignalr.utils import get_connection_url
from pysignalr.utils import get_negotiate_url
from pysignalr.utils import replace_scheme

DEFAULT_MAX_SIZE = 2 ** 20  # 1 MB
DEFAULT_PING_INTERVAL = 10
DEFAULT_CONNECTION_TIMEOUT = 10

_logger = logging.getLogger('pysignalr.transport')
_logger.setLevel(logging.DEBUG)


class CustomWebsocketTransport(Transport):
    reconnect = True

    def __init__(
            self,
            url: str,
            ssl_context: ssl.SSLContext,
            protocol: Protocol,
            callback: Callable[[Message], Awaitable[None]],
            headers: Optional[Dict[str, str]] = None,
            skip_negotiation: bool = False,
            ping_interval: int = DEFAULT_PING_INTERVAL,
            connection_timeout: int = DEFAULT_CONNECTION_TIMEOUT,
            max_size: Optional[int] = DEFAULT_MAX_SIZE,
    ):
        super().__init__()
        self._url = url
        self._ssl_context = ssl_context
        self._protocol = protocol
        self._callback = callback
        self._headers = headers or {}
        self._skip_negotiation = skip_negotiation
        self._ping_interval = ping_interval
        self._connection_timeout = connection_timeout
        self._max_size = max_size

        self._state = ConnectionState.disconnected
        self._connected = asyncio.Event()
        self._ws: Optional[WebSocketClientProtocol] = None
        self._open_callback: Optional[Callable[[], Awaitable[None]]] = None
        self._close_callback: Optional[Callable[[], Awaitable[None]]] = None

    async def close(self) -> None:
        self.reconnect = False
        if self._ws:
            try:
                await self._ws.close()
            except Exception:
                pass

    def on_open(self, callback: Callable[[], Awaitable[None]]) -> None:
        self._open_callback = callback

    def on_close(self, callback: Callable[[], Awaitable[None]]) -> None:
        self._close_callback = callback

    def on_error(self, callback: Callable[[CompletionMessage], Awaitable[None]]) -> None:
        self._error_callback = callback

    async def run(self) -> None:
        self.reconnect = True
        while True:
            if not self.reconnect:
                return
            with suppress(NegotiationTimeout):
                await self._loop()
            await self._set_state(ConnectionState.disconnected)


    async def send(self, message: Message) -> None:
        conn = await self._get_connection()
        await conn.send(self._protocol.encode(message))

    async def _loop(self) -> None:
        await self._set_state(ConnectionState.connecting)

        if not self._skip_negotiation:
            try:
                await self._negotiate()
            except ServerConnectionError as e:
                raise NegotiationTimeout from e

        self.connection_loop = connect(
            self._url,
            extra_headers=self._headers,
            ping_interval=self._ping_interval,
            open_timeout=self._connection_timeout,
            max_size=self._max_size,
            logger=_logger,
            ssl=self._ssl_context
        )

        async for conn in self.connection_loop:
            try:
                await self._handshake(conn)
                self._ws = conn
                await self._set_state(ConnectionState.connected)
                await asyncio.gather(
                    self._process(conn),
                    self._keepalive(conn),
                )

            except ConnectionClosed as e:
                _logger.warning('Connection closed: %s', e)
                self._ws = None
                if self.reconnect:
                    await self._set_state(ConnectionState.reconnecting)
                else:
                    await self._set_state(ConnectionState.disconnected)

    async def _set_state(self, state: ConnectionState) -> None:
        if state == self._state:
            return

        _logger.info('State change: %s -> %s', self._state.name, state.name)

        if state == ConnectionState.connecting:
            if self._state != ConnectionState.disconnected:
                raise RuntimeError('Cannot connect while not disconnected')

            self._connected.clear()

        elif state == ConnectionState.connected:
            if self._state not in (ConnectionState.connecting, ConnectionState.reconnecting):
                raise RuntimeError('Cannot connect while not connecting or reconnecting')

            self._connected.set()

            if self._open_callback:
                await self._open_callback()

        elif state in (ConnectionState.reconnecting, ConnectionState.disconnected):
            self._connected.clear()

            if self._close_callback:
                await self._close_callback()

        else:
            raise NotImplementedError

        self._state = state

    async def _get_connection(self) -> WebSocketClientProtocol:
        await self._connected.wait()
        if not self._ws or self._ws.state != State.OPEN:
            raise RuntimeError('Connection is closed')
        return self._ws

    async def _process(self, conn: WebSocketClientProtocol) -> None:
        while True:
            raw_message = await conn.recv()
            await self._on_raw_message(raw_message)

    async def _keepalive(self, conn: WebSocketClientProtocol) -> None:
        while True:
            await asyncio.sleep(10)
            await conn.send(self._protocol.encode(PingMessage()))

    async def _handshake(self, conn: WebSocketClientProtocol) -> None:
        _logger.info('Sending handshake to server')
        our_handshake = self._protocol.handshake_message()
        await conn.send(self._protocol.encode(our_handshake))

        _logger.info('Awaiting handshake from server')
        raw_message = await conn.recv()
        handshake, messages = self._protocol.decode_handshake(raw_message)
        if handshake.error:
            raise ValueError(f'Handshake error: {handshake.error}')
        for message in messages:
            await self._on_message(message)

    async def _negotiate(self) -> None:
        negotiate_url = get_negotiate_url(self._url)
        _logger.info('Performing negotiation, URL: `%s`', negotiate_url)

        conn = TCPConnector(ssl_context=self._ssl_context)
        session = ClientSession(
            timeout=ClientTimeout(connect=self._connection_timeout),
            connector=conn)

        async with session:
            async with session.post(negotiate_url, headers=self._headers) as response:
                if response.status == HTTPStatus.OK:
                    data = await response.json()
                elif response.status == HTTPStatus.UNAUTHORIZED:
                    raise exceptions.AuthorizationError
                else:
                    raise exceptions.ConnectionError(response.status)

        connection_id = data.get('connectionId')
        url = data.get('url')
        access_token = data.get('accessToken')

        if connection_id:
            _logger.info('Negotiation completed')
            self._url = get_connection_url(self._url, connection_id)
        elif url and access_token:
            _logger.info('Negotiation completed (Azure)')
            self._url = replace_scheme(url, ws=True)
            self._headers['Authorization'] = f'Bearer {access_token}'
        else:
            raise exceptions.ServerError(str(data))

    async def _on_raw_message(self, raw_message: Union[str, bytes]) -> None:
        for message in self._protocol.decode(raw_message):
            await self._on_message(message)

    async def _on_message(self, message: Message) -> None:
        await self._callback(message)
