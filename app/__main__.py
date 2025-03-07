from time import sleep

from lib import some_lib_func

from .app_logging import LOGGER, LOGGING_CONFIGURATION


def run_app(display: str) -> None:
    LOGGING_CONFIGURATION.set_configuration()
    LOGGER.info("Starting application")
    sleep(1)
    LOGGER.info("Started!")
    result = some_lib_func()
    LOGGER.warning(f"Got: {result}")
    print(display)
    LOGGER.info(f"Displayed: {display=}", display=display)
    LOGGER.info("Terminating...")


run_app("My display text!")
