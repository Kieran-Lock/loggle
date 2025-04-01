from ..lib.schemas import FormatterSchema
from ..lib import FormatterFactory
from ..json_formatter import JSONFormatter
from ..standard_formatter import StandardFormatter


class Formatters:
    STANDARD = FormatterSchema(formatter_factory=FormatterFactory(lambda: StandardFormatter()))
    JSON = FormatterSchema(formatter_factory=FormatterFactory(lambda: JSONFormatter()))
