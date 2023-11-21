from flask import Blueprint
from flask import current_app as app


health_bp = Blueprint('health', __name__, url_prefix="/health")


@health_bp.route('', methods=['GET'])
def health():
    app.logger.info('health.infrastructure.routes#health - API health is OK')
    return {'message': 'API health is OK'}, 200
