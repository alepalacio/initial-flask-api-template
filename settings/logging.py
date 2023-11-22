from settings.config import Configuration
import logging

# Common base logging configuration
logging.basicConfig(
    filename=Configuration.LOGGING_LOCATION,
    level=Configuration.LOGGING_LEVEL,
    format=Configuration.LOGGING_FORMAT
    )
handler = logging.StreamHandler()
handler.setLevel(Configuration.LOGGING_LEVEL)
formatter = logging.Formatter(Configuration.LOGGING_FORMAT)
handler.setFormatter(formatter)