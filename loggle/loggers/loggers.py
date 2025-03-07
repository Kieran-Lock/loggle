from .lib.schemas import LoggersSchema, LoggerSchema
from ..handlers.lib.types import QueueHandlerName
from ..lib.consts import LoggingLevel
from .lib.consts import DefaultLoggerName


UVICORN_LOGGERS = LoggersSchema(
    loggers={
        DefaultLoggerName.UVICORN: LoggerSchema(
            handlers=[QueueHandlerName.QUEUE],
            level=LoggingLevel.INFO,
            propagate=False,
        ),
        DefaultLoggerName.UVICORN_ACCESS: LoggerSchema(
            handlers=[QueueHandlerName.QUEUE],
            level=LoggingLevel.INFO,
            propagate=False,
        ),
        DefaultLoggerName.UVICORN_ERROR: LoggerSchema(
            handlers=[QueueHandlerName.QUEUE],
            level=LoggingLevel.INFO,
            propagate=False,
        ),
        DefaultLoggerName.UVICORN_ASGI: LoggerSchema(
            handlers=[QueueHandlerName.QUEUE],
            level=LoggingLevel.INFO,
            propagate=False,
        ),
    }
).to_loggers_dictionary()
