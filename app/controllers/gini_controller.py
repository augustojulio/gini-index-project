from flask import Blueprint
from app.services.gini_service import GiniService

gini_blueprint = Blueprint('gini', __name__)

@gini_blueprint.route('/process', methods=['POST'])
def process_gini():
    service = GiniService()
    service.process_files()
    return {"status": "success"}, 200
