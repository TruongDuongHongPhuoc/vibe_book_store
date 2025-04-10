from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mySecrect'  # Replace with a secure value
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Set up file upload settings
    app.config['UPLOAD_FOLDER'] = 'uploads'  # Folder where the files will be stored
    app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'epub'}  # Allowed file extensions

    db.init_app(app)

    # Import the routes after initializing the app
    with app.app_context():
        from app.models.test import Test
        from app.models.category_model import Category
        from app.models.reader_model import Reader
        from app.models.book_model import Book
        from app.models.comment_model import Comment
        from app.models.cart_model import Cart
        db.create_all()

        


        from app.routes.test_routes import test_routes
        from app.routes.category_routes import category_routes
        from app.routes.reader_routes import reader_routes
        from app.routes.auth_routes import auth_routes
        from app.routes.book_routes import book_routes
        from app.routes.cart_routes import cart_routes

        app.register_blueprint(book_routes)
        app.register_blueprint(auth_routes)
        app.register_blueprint(reader_routes)
        app.register_blueprint(category_routes)
        app.register_blueprint(test_routes)
        app.register_blueprint(cart_routes)

    return app
