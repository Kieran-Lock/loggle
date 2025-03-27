from typing import overload, Any

from pydantic_core import CoreSchema, core_schema
from pydantic import GetCoreSchemaHandler

from .consts import BasePrimaryHandlerName, PrimaryHandlerName, SecondaryHandlerName, BaseSecondaryHandlerName
from .schemas import HandlerModel, StreamHandlerSchema, FileHandlerSchema, QueueHandlerSchema
from ...formatters.lib.consts import FormatterName


type HandlerName = PrimaryHandlerName | SecondaryHandlerName
type BaseHandlerName = BasePrimaryHandlerName | BaseSecondaryHandlerName
type PHandler = StreamHandlerSchema[FormatterName] | FileHandlerSchema[FormatterName]
type SHandler = QueueHandlerSchema[PrimaryHandlerName]


class HandlersDict[K: HandlerName, V_PHandler: HandlerModel, V_SHandler: HandlerModel](dict[K, V_PHandler | V_SHandler]):
    @overload
    def __getitem__(self, key: PrimaryHandlerName) -> V_PHandler:
        ...
    
    @overload
    def __getitem__(self, key: SecondaryHandlerName) -> V_SHandler:
        ...

    def __getitem__(self, key: K) -> V_PHandler | V_SHandler:
        return super(HandlersDict, self).__getitem__(key)
    
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler: GetCoreSchemaHandler) -> CoreSchema:
        return core_schema.no_info_after_validator_function(cls, handler(dict))
