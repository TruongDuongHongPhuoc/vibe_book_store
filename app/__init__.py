from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Import the routes after initializing the app
    with app.app_context():
        from app.models.test import Test
        from app.models.category_model import Category
        from app.models.reader_model import Reader
        db.create_all()

        from app.routes.test_routes import test_routes
        from app.routes.category_routes import category_routes
        from app.routes.reader_routes import reader_routes
        app.register_blueprint(reader_routes)
        app.register_blueprint(category_routes)
        app.register_blueprint(test_routes)

    return app
