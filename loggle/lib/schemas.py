from __future__ import annotations

from typing import Literal, Self, Any
from logging.config import dictConfig as dict_config
from pydantic import BaseModel

from ..handlers import QueueHandler
from ..formatters.lib.schemas import FormatterSchema
from ..formatters.lib.consts import FormatterName
from ..handlers.lib.types import HandlerName, HandlerSchema
from ..handlers.lib.consts import QueueHandlerName
from ..loggers.lib.consts import LoggerName
from ..loggers.lib.schemas import LoggerSchema


class LoggingConfiguration(BaseModel):
    version: Literal[1]
    disable_existing_loggers: bool
    formatters: dict[FormatterName, FormatterSchema]
    handlers: dict[HandlerName, HandlerSchema]
    loggers: dict[LoggerName, LoggerSchema]

    def set_configuration(self) -> None:
        dict_config(self.to_configuration_dictionary())
        if QueueHandlerName.QUEUE in self.handlers:
            QueueHandler.get().start_listener()
    
    def to_configuration_dictionary(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True, by_alias=True)

    @classmethod
    def default(
        cls,
        *,
        formatters: dict[FormatterName, FormatterSchema],
        handlers: dict[HandlerName, HandlerSchema],
        loggers: dict[LoggerName, LoggerSchema],
    ) -> Self:
        return cls(
            version=1,
            disable_existing_loggers=True,
            formatters=formatters,
            handlers=handlers,
            loggers=loggers,
        )
