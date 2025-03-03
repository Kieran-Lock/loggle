from enum import StrEnum
from logging import CRITICAL, FATAL, ERROR, WARN, WARNING, INFO, DEBUG, NOTSET, _levelToName


class LoggingLevel(StrEnum):
    CRITICAL = _levelToName[CRITICAL]
    FATAL = _levelToName[FATAL]
    ERROR = _levelToName[ERROR]
    WARN = _levelToName[WARN]
    WARNING = _levelToName[WARNING]
    INFO = _levelToName[INFO]
    DEBUG = _levelToName[DEBUG]
    NOTSET = _levelToName[NOTSET]
