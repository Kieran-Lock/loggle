from enum import StrEnum


class LoggerName(StrEnum):
    pass


class UvicornLoggerName(StrEnum):
    UVICORN = "uvicorn"
    UVICORN_ACCESS = "uvicorn.access"
    UVICORN_ERROR = "uvicorn.error"
    UVICORN_ASGI = "uvicorn.asgi"
