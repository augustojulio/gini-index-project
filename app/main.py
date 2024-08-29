from flask import Flask
from app.config import Config
from app.models import db
from app.controllers.gini_controller import gini_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(gini_blueprint, url_prefix='/gini')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
