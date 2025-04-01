from logging.handlers import QueueHandler as DefaultQueueHandler, QueueListener
from atexit import register as at_exit_register
from typing import Self, ClassVar, Literal
from multiprocessing import Queue
from dataclasses import dataclass


@dataclass(slots=True, init=False)
class QueueHandler(DefaultQueueHandler):
    AUTOMATICALLY_SET_LISTENER: ClassVar[bool] = False

    queue: Queue
    _listener: QueueListener | None
    _is_configuring_by_dictionary: bool

    def __init__(self, queue: Queue, *, _is_dictionary_configuration: bool = False) -> None:
        self.queue = queue
        self._listener = None
        self._is_configuring_by_dictionary = _is_dictionary_configuration
        super(QueueHandler, self).__init__(queue)
    
    @property
    def listener(self) -> QueueListener | None:
        return self._listener
    
    @listener.setter
    def listener(self, value: QueueListener | None) -> None:  # TODO: Tidy up queue handler
        self._listener = value
        if self._is_configuring_by_dictionary and self.AUTOMATICALLY_SET_LISTENER and isinstance(value, QueueListener):
            self._is_configuring_by_dictionary = False
            self.start_listener()
    
    @classmethod
    def automatically_set_listener(cls) -> None:
        cls.AUTOMATICALLY_SET_LISTENER = True

    def start_listener(self) -> None:
        self.listener.start()
        at_exit_register(self.listener.stop)
    
    def __hash__(self) -> int:
        return super(QueueHandler, self).__hash__()
