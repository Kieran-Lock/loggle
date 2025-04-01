from time import sleep
from pprint import pprint

from lib import some_lib_func

from .app_logging import LOGGER, LOGGING_CONFIGURATION


def run_app(display: str) -> None:
    pprint(LOGGING_CONFIGURATION.to_configuration_dictionary())
    LOGGING_CONFIGURATION.set_configuration()
    LOGGER.info("Starting application")
    sleep(1)
    LOGGER.info("Started!")
    result_one = some_lib_func()
    LOGGER.warning(f"Got: {result_one}")
    print(display)
    result_two = some_lib_func(n=6)
    LOGGER.warning(f"Got: {result_two}")
    LOGGER.info(f"Displayed: {display=}", display=display)
    LOGGER.info("Terminating...")


run_app("My display text!")
