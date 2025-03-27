from logging import StreamHandler
from pathlib import Path

from .lib.consts import PrimaryHandlerName, SecondaryHandlerName, LoggingStream, MAXIMUM_LOG_FILE_BYTES, LOG_FILE_BACKUPS
from .lib.schemas import StreamHandlerSchema, FileHandlerSchema, QueueHandlerSchema
from .lib.types import HandlerName, PHandler, SHandler, HandlersDict
from ..formatters.lib.consts import FormatterName
from ..lib.consts import LoggingLevel
from .queue_handler import QueueHandler
from .json_file_handler import JSONFileHandler
from ..filters import FilterName


QueueHandler.automatically_set_listener()


LOGGLE_HANDLERS = HandlersDict[HandlerName, PHandler, SHandler]({
    PrimaryHandlerName.STANDARD: StreamHandlerSchema(
        handler_class=StreamHandler,
        filters=[FilterName.ERROR],
        formatter=FormatterName.STANDARD,
        level=LoggingLevel.DEBUG,
        stream=LoggingStream.STANDARD_OUT,
    ),
    PrimaryHandlerName.ERROR: StreamHandlerSchema(
        handler_class=StreamHandler,
        formatter=FormatterName.STANDARD,
        level=LoggingLevel.ERROR,
        stream=LoggingStream.STANDARD_ERROR,
    ),
    PrimaryHandlerName.JSON_FILE: FileHandlerSchema(
        handler_class=JSONFileHandler,
        formatter=FormatterName.JSON,
        level=LoggingLevel.DEBUG,
        filename=Path(f"./logging/logs/log.{JSONFileHandler.FILE_EXTENSION}"),
        max_bytes=MAXIMUM_LOG_FILE_BYTES,
        backup_count=LOG_FILE_BACKUPS,
    ),
    SecondaryHandlerName.QUEUE: QueueHandlerSchema(
        handler_class=QueueHandler,
        handlers=[
            PrimaryHandlerName.STANDARD,
            PrimaryHandlerName.ERROR,
            PrimaryHandlerName.JSON_FILE,
        ],
    ),
})
