from .lib.schemas import LoggersSchema, LoggerSchema
from ..handlers import SecondaryHandlerName
from ..lib.consts import LoggingLevel
from .lib.consts import LoggerName


UVICORN_LOGGERS = LoggersSchema(
    loggers={
        LoggerName.UVICORN: LoggerSchema(
            handlers=[SecondaryHandlerName.QUEUE],
            level=LoggingLevel.INFO,
            propagate=False,
        ),
        LoggerName.UVICORN_ACCESS: LoggerSchema(
            handlers=[SecondaryHandlerName.QUEUE],
            level=LoggingLevel.INFO,
            propagate=False,
        ),
        LoggerName.UVICORN_ERROR: LoggerSchema(
            handlers=[SecondaryHandlerName.QUEUE],
            level=LoggingLevel.INFO,
            propagate=False,
        ),
        LoggerName.UVICORN_ASGI: LoggerSchema(
            handlers=[SecondaryHandlerName.QUEUE],
            level=LoggingLevel.INFO,
            propagate=False,
        ),
    }
).to_loggers_dictionary()
