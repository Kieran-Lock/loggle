from __future__ import annotations

from typing import Literal, Self, Any
from logging.config import dictConfig as dict_config
from pydantic import BaseModel

from ..handlers import QueueHandler
from ..filters import BaseFilterName, FilterSchema, LOGGLE_FILTERS
from ..formatters import FormatterSchema, BaseFormatterName, LOGGLE_FORMATTERS
from ..handlers import HandlerName, SecondaryHandlerName, BaseHandlerName, LOGGLE_HANDLERS, HandlersDict, HandlerModel
from ..loggers import BaseLoggerName, LoggerSchema, LoggersSchema


class LoggingConfiguration[T_FilterName: BaseFilterName, T_FormatterName: BaseFormatterName, T_HandlerName: BaseHandlerName, T_PHandler: HandlerModel, T_SHandler: HandlerModel, T_LName: BaseLoggerName](BaseModel):
    version: Literal[1]
    disable_existing_loggers: bool
    filters: dict[T_FilterName, FilterSchema]
    formatters: dict[T_FormatterName, FormatterSchema]
    handlers: HandlersDict[T_HandlerName, T_PHandler, T_SHandler]
    loggers: dict[T_LName, LoggerSchema[T_HandlerName]]

    def set_configuration(self) -> None:
        dict_config(self.to_configuration_dictionary())  # TODO: Investigate how this works!
    
    def to_configuration_dictionary(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True, by_alias=True)

    @classmethod
    def create(
        cls,
        *,
        filters: dict[T_FilterName, FilterSchema],
        formatters: dict[T_FormatterName, FormatterSchema],
        handlers: HandlersDict[T_HandlerName, T_PHandler, T_SHandler],
        loggers: LoggersSchema[T_LName, T_HandlerName] | dict[T_LName, LoggerSchema[T_HandlerName]],
    ) -> Self:
        return cls(
            version=1,
            disable_existing_loggers=True,
            filters=filters,
            formatters=formatters,
            handlers=handlers,
            loggers=loggers.to_loggers_dictionary() if isinstance(loggers, LoggersSchema) else loggers,
        )
    
    @classmethod
    def default(cls, *, loggers: LoggersSchema[T_LName, T_HandlerName] | dict[T_LName, LoggerSchema[T_HandlerName]]) -> Self:
        return cls.create(
            filters=LOGGLE_FILTERS,
            formatters=LOGGLE_FORMATTERS,
            handlers=LOGGLE_HANDLERS,
            loggers=loggers,
        )
