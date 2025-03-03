from .lib.schemas import LoggingConfiguration
from .formatters import FORMATTERS
from .handlers import HANDLERS
from .loggers import UVICORN_LOGGERS


LOGGING_CONFIGURATION = LoggingConfiguration.default(
    formatters=FORMATTERS,
    handlers=HANDLERS,
    loggers=UVICORN_LOGGERS.to_loggers_dictionary(),
)
