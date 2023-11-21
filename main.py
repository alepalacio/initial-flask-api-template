from flask import Flask

from app.health.infrastructure.routes import health_bp

from settings.config import Configuration
import logging

# Application initialization
app = Flask(__name__)
app.config.from_object(Configuration)

# Logging configuration
logging.basicConfig(filename=app.config['LOGGING_LOCATION'],
                    level=app.config['LOGGING_LEVEL'],
                    format=app.config['LOGGING_FORMAT'])
handler = logging.StreamHandler()
handler.setLevel(app.config['LOGGING_LEVEL'])
formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
handler.setFormatter(formatter)
app.logger.addHandler(handler)


# Views
app.register_blueprint(health_bp)

if __name__ == "__main__":
    app.run(
        host=app.config.get("DOMAIN"),
        port=app.config.get("PORT")
    )
