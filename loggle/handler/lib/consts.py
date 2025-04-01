from enum import StrEnum


MEBI = 1_024 * 1_024
DEFAULT_MAXIMUM_LOG_FILE_BYTES = 10 * MEBI
DEFAULT_LOG_FILE_BACKUPS = 3


class LoggingStream(StrEnum):
    STANDARD_OUT = "ext://sys.stdout"
    STANDARD_ERROR = "ext://sys.stderr"


class AtomicHandlerName(StrEnum):
    pass


class CompositeHandlerName(StrEnum):
    pass
