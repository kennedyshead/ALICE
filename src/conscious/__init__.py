"""
Conscious module to handle processing and abstract thought
"""
import logging
from enum import Enum
from queue import Queue


class Event(str, Enum):
    """
    Event enum, used to send events in queue
    """

    NEW_TEXT = "Text Received"


class Conscious:
    """
    Conscious class to handle processing and abstract thought
    """

    @classmethod
    async def loop(cls, queue: Queue) -> None:
        """
        Conscious loop
        :return:
        """
        logging.info("I'm conscious")
        while True:
            await cls.process_input(queue)

    @classmethod
    async def process_input(cls, queue: Queue) -> None:
        """
        Handle the input
        :return:
        """
        task = queue.get()
        logging.info(task)
        queue.task_done()
