from .consts import StreamHandlerName, FileHandlerName, QueueHandlerName
from .schemas import StreamHandlerSchema, FileHandlerSchema, QueueHandlerSchema


type PrimaryHandlerName = StreamHandlerName | FileHandlerName
type HandlerName = PrimaryHandlerName | QueueHandlerName

type PrimaryHandlerSchema = StreamHandlerSchema | FileHandlerSchema
type HandlerSchema = PrimaryHandlerSchema | QueueHandlerSchema
