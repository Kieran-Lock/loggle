from pathlib import Path

from loggle import LoggingConfiguration, Logger, LoggersSchema, LoggerName


class AppLoggerName(LoggerName):
    MY_LIBRARY = "my-library"
    MY_APPLICATION = "my-application"


LOGGING_CONFIGURATION = LoggingConfiguration.default(loggers=LoggersSchema.from_json(Path("./loggers.json")))
LOGGER = Logger(name=AppLoggerName.MY_APPLICATION)
