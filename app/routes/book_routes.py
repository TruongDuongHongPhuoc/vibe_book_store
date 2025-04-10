from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.repositories import book_repo
from app.repositories.book_repo import BookRepository
from app.models import book_model, category_model, reader_model, comment_model
from app.models.comment_model import Comment
from app.models.reader_model import Reader
from app.models.category_model import Category
from datetime import datetime
from app.repositories.comment_repo import CommentRepository
import os
from werkzeug.utils import secure_filename

book_routes = Blueprint('book_routes', __name__)
# Define upload directories
UPLOAD_FOLDER_IMAGES = 'app/static/uploads/images'
UPLOAD_FOLDER_BOOKS = 'app/static/uploads/books'


# Create directories if they do not exist
os.makedirs(UPLOAD_FOLDER_IMAGES, exist_ok=True)
os.makedirs(UPLOAD_FOLDER_BOOKS, exist_ok=True)

# Helper function to check file extension
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'epub'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# List all books
@book_routes.route('/books', methods=['GET'])
def list_books():
    books = BookRepository.get_all_books()
    return render_template('book/book_list.html', books=books)

@book_routes.route('/books/create', methods=['GET', 'POST'])
def create_book():
    if request.method == 'POST':
        # Get uploaded files
        cover_image = request.files.get('cover_image')
        book_file = request.files.get('book_file')

        # Define folder paths
        image_folder = os.path.join('uploads', 'images', 'books')
        book_folder = os.path.join('uploads', 'books')

        # Ensure folders exist
        os.makedirs(image_folder, exist_ok=True)
        os.makedirs(book_folder, exist_ok=True)

        # Save cover image
        if cover_image and allowed_file(cover_image.filename):
            image_filename = secure_filename(cover_image.filename)
            image_path = os.path.join(UPLOAD_FOLDER_IMAGES, image_filename)  # Save in static/uploads/images
            cover_image.save(image_path)
        else:
            return "Cover image is required and must be valid", 400

        # Save book file (if available)
        if book_file and allowed_file(book_file.filename):
            book_filename = secure_filename(book_file.filename)
            book_file_path = os.path.join(UPLOAD_FOLDER_BOOKS, book_filename)
            book_file.save(book_file_path)
        else:
            book_file_path = None

       # Store only the relative path for cover image
        book_data = {
            'title': request.form['title'],
            'description': request.form['description'],
            'category_id': request.form['category_id'],
            'author_id': request.form['author_id'],
            'published': datetime.strptime(request.form['published'], '%Y-%m-%d'),
            'quantity': request.form['quantity'],
            'cover_image_path': os.path.join('uploads', 'images', image_filename).replace("\\", "/"),
            'file': os.path.join('uploads', 'books', book_filename).replace("\\", "/"),
            'full_pay_price': request.form['fullpay_price'],
            'rent_price': request.form['rent_price']
        }

        BookRepository.add_book(book_data)
        return redirect(url_for('book_routes.list_books'))

    # GET method
    categories = Category.query.all()
    readers = Reader.query.filter_by(role=2).all()
    return render_template('book/book_create.html', categories=categories, readers=readers)




# Edit a book
@book_routes.route('/books/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = BookRepository.get_book_by_id(book_id)
    if not book:
        return redirect(url_for('book_routes.list_books'))  # If book not found, go back to list

    if request.method == 'POST':
        # Handle file uploads for cover image and book file
        cover_image = request.files.get('cover_image')
        book_file = request.files.get('book_file')

        # Handle cover image upload
        if cover_image and allowed_file(cover_image.filename):
            image_filename = secure_filename(cover_image.filename)
            image_path = os.path.join('uploads', 'images', image_filename).replace("\\", "/")  # Save in static/uploads/images
            cover_image.save(image_path)
        else:
            image_path = book.cover_image_path  # Keep the existing image path if no new image is uploaded

        # Handle book file upload
        if book_file and allowed_file(book_file.filename):
            book_filename = secure_filename(book_file.filename)
            book_file_path = os.path.join('uploads', 'books', book_filename).replace("\\", "/")  # Save in static/uploads/books
            book_file.save(book_file_path)
        else:
            book_file_path = book.file  # Keep the existing file path if no new file is uploaded

        # Prepare updated book data
        book_data = {
            'title': request.form['title'],
            'description': request.form['description'],
            'category_id': request.form['category_id'],
            'author_id': request.form['author_id'],
            'published': datetime.strptime(request.form['published'], '%Y-%m-%d'),
            'quantity': request.form['quantity'],
            'cover_image_path': image_path,  # Store cover image path
            'file': book_file_path,  # Store book file path
            'full_pay_price': request.form['fullpay_price'],
            'rent_price': request.form['rent_price']
        }

        # Update the book in the repository
        BookRepository.update_book(book_id, book_data)
        return redirect(url_for('book_routes.list_books'))

    # Fetch categories and readers
    categories = Category.query.all()
    readers = Reader.query.filter_by(role=2).all()
    return render_template('book/book_edit.html', book=book, categories=categories, readers=readers)

# Delete a book
@book_routes.route('/books/delete/<int:book_id>', methods=['GET'])
def delete_book(book_id):
    BookRepository.delete_book(book_id)
    return redirect(url_for('book_routes.list_books'))

# Book detail and comments
@book_routes.route('/books/<int:book_id>', methods=['GET', 'POST'])
def book_detail(book_id):
    book = BookRepository.get_book_by_id(book_id)
    if not book:
        return "Book not found", 404

    if request.method == 'POST':
        content = request.form['content']
        reader_id = request.form['reader_id']  # Pass this via hidden input or session
        comment_data = {'book_id': book_id, 'reader_id': reader_id, 'content': content}
        CommentRepository.add_comment(comment_data)
        return redirect(url_for('book_routes.book_detail', book_id=book_id))

    comments = CommentRepository.get_comments_by_book(book_id)
    return render_template('book/book_detail.html', book=book, comments=comments)

# Delete a comment
@book_routes.route('/comments/delete/<int:comment_id>', methods=['POST'])
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if comment:
        book_id = comment.book_id
        CommentRepository.delete_comment(comment_id)
        return redirect(url_for('book_routes.book_detail', book_id=book_id))
    return "Comment not found", 404

@book_routes.route('/')
def homepage():
    # Query all books from the database
    books = BookRepository.get_books_litmited_by_six()
    categories = Category.query.all()
    # Render the homepage template and pass the books to the template
    return render_template('Homepage/home.html', books=books, categories=categories)

@book_routes.route('/books/load')
def load_more_books():
    offset = int(request.args.get('offset', 0))
    limit = int(request.args.get('limit', 6))

    books = BookRepository.get_books_offset_limit(offset, limit)

    book_list = []
    for book in books:
        book_list.append({
            'id': book.id,
            'title': book.title,
            'description': book.description,
            'cover_image_path': url_for('static', filename=book.cover_image_path),
            'author': book.author.full_name if book.author else 'Unknown',
            'full_pay_price': book.full_pay_price
        })

    return jsonify(book_list)
