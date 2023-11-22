from decouple import config
import logging


class Configuration:
    ENVIRONMENT = config("ENV", default="staging")
    DOMAIN = config("DOMAIN", default="0.0.0.0")
    PORT = config("PORT", default=9000, cast=int)
    DEBUG = config("DEBUG", default=False, cast=bool)
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="")
    LOGGING_FORMAT = '%(asctime)s %(levelname)s [%(name)s:%(funcName)s:%(lineno)d] %(message)s'
    LOGGING_LOCATION = 'application.log'
    LOGGING_LEVEL = logging.INFO
    OPENAPI_DOCS_URL = config("OPENAPI_DOCS_URL", default="/api/v1/docs") if ENVIRONMENT == 'staging' else None
    OPENAPI_SCHEMA_URL = "/static/openapi.json" if ENVIRONMENT == 'staging' else None
    OPENAPI_APP_NAME = config("OPENAPI_APP_NAME", default="API Documentation")
