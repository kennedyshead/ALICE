"""
Keystrokes AKA keyboard input
"""
import asyncio
import json
import sys
from asyncio import AbstractEventLoop, StreamReader
from queue import Queue
from typing import TextIO

from conscious import Event


class KeyBoard:
    """
    class for keystrokes AKA keyboard input
    """

    @staticmethod
    async def listen(queue: Queue) -> None:
        """
        Keyboard listener
        :return:
        """
        reader: StreamReader = StreamReader()
        pipe: TextIO = sys.stdin
        loop: AbstractEventLoop = asyncio.get_event_loop()
        await loop.connect_read_pipe(
            lambda: asyncio.StreamReaderProtocol(reader), pipe
        )

        async for line in reader:
            decoded: str = line.decode().strip("\n")
            queue.put(
                json.dumps(
                    {
                        "message": decoded,
                        "event": Event.NEW_TEXT,
                    }
                )
            )

    @classmethod
    async def loop(cls, queue: Queue):
        """
        Keyboard loop
        :return:
        """
        await cls.listen(queue)
