from pathlib import Path

from loggle import LoggingConfiguration, Logger, LoggersSchema, LoggerName, FormatterName, AtomicHandlerName, CompositeHandlerName, AtomicHandlerSchema, CompositeHandlerSchema, FilterName
from loggle.collections import Filters, Formatters, Handlers


class AppFilterName(FilterName):
    ERROR = "ERROR"


class AppFormatterName(FormatterName):
    STANDARD = "STANDARD"
    JSON = "JSON"


class AppAtomicHandlerName(AtomicHandlerName):
    STANDARD = "STANDARD"
    JSON_FILE = "JSON_FILE"


class AppCompositeHandlerName(CompositeHandlerName):
    QUEUE = "QUEUE"


class AppLoggerName(LoggerName):
    MY_LIBRARY = "my-library"
    MY_APPLICATION = "my-application"


LOGGING_CONFIGURATION = (
    LoggingConfiguration[AppFilterName, AppFormatterName, AppAtomicHandlerName | AppCompositeHandlerName, AppLoggerName].create(
        filters={AppFilterName.ERROR: Filters.ERROR},
        formatters={AppFormatterName.STANDARD: Formatters.STANDARD, AppFormatterName.JSON: Formatters.JSON},
        handlers={AppAtomicHandlerName.STANDARD: Handlers.STANDARD, AppAtomicHandlerName.JSON_FILE: Handlers.JSON_FILE, AppCompositeHandlerName.QUEUE: Handlers.QUEUE},
        loggers=LoggersSchema[LoggerName, AppAtomicHandlerName | AppCompositeHandlerName].from_json(Path("./logging/loggers.json"))
    )
)
LOGGER = Logger(name=AppLoggerName.MY_APPLICATION)
