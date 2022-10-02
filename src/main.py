"""
Main start script
"""
import asyncio
import logging
import sys
from asyncio import AbstractEventLoop
from queue import Queue
from threading import Thread
from typing import Any, List, Tuple, Union

from conscious import Conscious
from senses import KeyBoard

multi: List[Any] = [Conscious, KeyBoard]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        # logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ],
)


async def work(cls: Union[Conscious, KeyBoard], queue: Queue):
    """
    Work starter
    :param queue:
    :param cls:
    :return:
    """
    while True:
        await cls.loop(queue)


def worker(cls: Union[Conscious, KeyBoard], queue: Queue) -> None:
    """
    Worker
    :param queue:
    :param cls: Worker class
    :return:
    """
    new_loop: AbstractEventLoop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    new_loop.run_until_complete(work(cls, queue))


def main() -> None:
    """
    main function
    :return:
    """
    threads: Tuple = ()
    queue: Queue = Queue()
    for _cls in multi:
        thread: Thread = Thread(target=worker, args=[_cls, queue])
        threads += (thread,)
        thread.start()


if __name__ == "__main__":
    main()
