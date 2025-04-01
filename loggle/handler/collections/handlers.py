from logging import StreamHandler
from functools import partial

from ..lib.consts import LoggingStream
from ..lib.schemas import StreamHandlerSchema, FileHandlerSchema, QueueHandlerSchema
from ...lib.consts import LoggingLevel
from ..queue_handler import QueueHandler
from ..json_file_handler import JSONFileHandler


QueueHandler.automatically_set_listener()  # TODO: Tidy up queue handler


class Handlers:
    STANDARD = partial(
        StreamHandlerSchema,
        handler_class=StreamHandler,
        level=LoggingLevel.DEBUG,
        stream=LoggingStream.STANDARD_OUT,
    )
    ERROR = partial(
        StreamHandlerSchema,
        handler_class=StreamHandler,
        level=LoggingLevel.ERROR,
        stream=LoggingStream.STANDARD_ERROR,
    )
    JSON_FILE = partial(
        FileHandlerSchema,
        handler_class=JSONFileHandler,
        level=LoggingLevel.DEBUG,
    )
    QUEUE = partial(
        QueueHandlerSchema,
        handler_class=QueueHandler,
    )
