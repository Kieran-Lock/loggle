from pathlib import Path

from loggle import LoggingConfiguration, Logger, LoggersSchema, BaseLoggerName, FormatterName, HandlerName, PHandler, SHandler


class LoggerName(BaseLoggerName):
    MY_LIBRARY = "my-library"
    MY_APPLICATION = "my-application"


LOGGING_CONFIGURATION = (
    LoggingConfiguration[FormatterName, HandlerName, PHandler, SHandler, LoggerName].default(
        loggers=LoggersSchema[LoggerName, HandlerName].from_json(Path("./logging/loggers.json"))
    )
)
LOGGER = Logger(name=LoggerName.MY_APPLICATION)
