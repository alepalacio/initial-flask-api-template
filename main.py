from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from app.health.infrastructure.routes import health_bp

from settings.config import Configuration
from settings.logging import handler

# Application initialization
app = Flask(__name__)
app.config.from_object(Configuration)

# Logging configuration
app.logger.addHandler(handler)

# Swagger configuration
app.static_url_path = "/static"
swaggerui_blueprint = get_swaggerui_blueprint(
    Configuration.OPENAPI_DOCS_URL,
    Configuration.OPENAPI_SCHEMA_URL,
    config = {
        "app_name": Configuration.OPENAPI_APP_NAME
    }
)

# Views
app.register_blueprint(swaggerui_blueprint)
app.register_blueprint(health_bp)


if __name__ == "__main__":
    app.run(
        host=app.config.get("DOMAIN"),
        port=app.config.get("PORT")
    )
