from enum import StrEnum


class BaseLoggerName(StrEnum):
    pass


class LoggerName(BaseLoggerName):
    UVICORN = "uvicorn"
    UVICORN_ACCESS = "uvicorn.access"
    UVICORN_ERROR = "uvicorn.error"
    UVICORN_ASGI = "uvicorn.asgi"
    APPLICATION = "application"
