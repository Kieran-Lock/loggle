from pathlib import Path

from loggle import LoggingConfiguration, Logger, LoggersSchema, LoggerName, FormatterName, AtomicHandlerName, CompositeHandlerName, StreamHandlerSchema, FileHandlerSchema, CompositeHandlerSchema, FilterName, LoggingLevel, LoggingStream
from loggle.collections import Filters, Formatters, HandlerClasses, UvicornLoggerName, SQLAlchemyLoggerName


class AppFilterName(FilterName):
    ERROR = "error"


class AppFormatterName(FormatterName):
    STANDARD = "standard"
    JSON = "json"


class AppAtomicHandlerName(AtomicHandlerName):
    STANDARD = "standard"
    ERROR = "error"
    JSON_FILE = "json_file"


class AppCompositeHandlerName(CompositeHandlerName):
    QUEUE = "queue"


class AppLoggerName(LoggerName):
    COURSEWORK = "coursework"
    UVICORN = UvicornLoggerName.ROOT
    UVICORN_ACCESS = UvicornLoggerName.ACCESS
    UVICORN_ERROR = UvicornLoggerName.ERROR
    UVICORN_ASGI = UvicornLoggerName.ASGI
    SQLALCHEMY_ENGINE = SQLAlchemyLoggerName.ENGINE
    SQLALCHEMY_POOL = SQLAlchemyLoggerName.POOL
    SQLALCHEMY_DIALECTS = SQLAlchemyLoggerName.DIALECTS
    SQLALCHEMY_ORM = SQLAlchemyLoggerName.ORM


LOGGING_CONFIGURATION = (
    LoggingConfiguration[AppFilterName, AppFormatterName, AppAtomicHandlerName, AppCompositeHandlerName, AppLoggerName].create(
        filters={
            AppFilterName.ERROR: Filters.ERROR,
        },
        formatters={
            AppFormatterName.STANDARD: Formatters.STANDARD,
            AppFormatterName.JSON: Formatters.JSON,
        },
        handlers={
            AppAtomicHandlerName.STANDARD: StreamHandlerSchema(
                handler_class=HandlerClasses.STREAM,
                filters=[AppFilterName.ERROR],
                formatter=AppFormatterName.STANDARD,
                level=LoggingLevel.DEBUG,
                stream=LoggingStream.STANDARD_OUT,
            ),
            AppAtomicHandlerName.ERROR: StreamHandlerSchema(
                handler_class=HandlerClasses.STREAM,
                formatter=AppFormatterName.STANDARD,
                level=LoggingLevel.ERROR,
                stream=LoggingStream.STANDARD_ERROR,
            ),
            AppAtomicHandlerName.JSON_FILE: FileHandlerSchema(
                handler_class=HandlerClasses.JSON_FILE,
                formatter=AppFormatterName.JSON,
                level=LoggingLevel.DEBUG,
            ),
            AppCompositeHandlerName.QUEUE: CompositeHandlerSchema(
                handler_class=HandlerClasses.QUEUE,
                handlers=list(AppAtomicHandlerName),
            ),
        },
        loggers={},
    )
)
LOGGER = Logger(name=AppLoggerName.COURSEWORK)
