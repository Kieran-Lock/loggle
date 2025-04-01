from functools import partial

from ..lib.schemas import LoggerSchema


class Loggers:
    UVICORN = partial(
        LoggerSchema,
        propagate=False,
    )
    UVICORN_ACCESS = partial(
        LoggerSchema,
        propagate=False,
    )
    UVICORN_ERROR = partial(
        LoggerSchema,
        propagate=False,
    )
    UVICORN_ASGI = partial(
        LoggerSchema,
        propagate=False,
    )
