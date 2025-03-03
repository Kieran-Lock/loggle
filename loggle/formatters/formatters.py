from .lib.consts import FormatterName
from .lib.schemas import FormatterSchema
from .lib import FormatterFactory
from .json_formatter import JSONFormatter
from .standard_formatter import StandardFormatter


FORMATTERS = {
    FormatterName.STANDARD: FormatterSchema(
        formatter_factory=FormatterFactory(lambda: StandardFormatter()),
    ),
    FormatterName.JSON: FormatterSchema(
        formatter_factory=FormatterFactory(lambda: JSONFormatter()),
    ),
}
