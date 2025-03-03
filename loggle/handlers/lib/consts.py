from enum import StrEnum


MEBI = 1_024 * 1_024
MAXIMUM_LOG_FILE_BYTES = 10 * MEBI
LOG_FILE_BACKUPS = 3


class LoggingStream(StrEnum):
    STANDARD_OUT = "ext://sys.stdout"
    STANDARD_ERROR = "ext://sys.stderr"


class StreamHandlerName(StrEnum):
    STANDARD = "standard"
    ERROR = "error"


class FileHandlerName(StrEnum):
    JSON_FILE = "json_file"


class QueueHandlerName(StrEnum):
    QUEUE = "queue"
