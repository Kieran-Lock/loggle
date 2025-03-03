from .lib.schemas import LoggersSchema, LoggerName, LoggerSchema
from ..handlers.lib.types import QueueHandlerName
from ..lib.consts import LoggingLevel


UVICORN_LOGGERS = LoggersSchema(
    loggers={
        LoggerName.UVICORN: LoggerSchema(
            handlers=[QueueHandlerName.QUEUE],
            level=LoggingLevel.INFO,
            propagate=False,
        ),
        LoggerName.UVICORN_ACCESS: LoggerSchema(
            handlers=[QueueHandlerName.QUEUE],
            level=LoggingLevel.INFO,
            propagate=False,
        ),
        LoggerName.UVICORN_ERROR: LoggerSchema(
            handlers=[QueueHandlerName.QUEUE],
            level=LoggingLevel.INFO,
            propagate=False,
        ),
        LoggerName.UVICORN_ASGI: LoggerSchema(
            handlers=[QueueHandlerName.QUEUE],
            level=LoggingLevel.INFO,
            propagate=False,
        ),
    }
)
