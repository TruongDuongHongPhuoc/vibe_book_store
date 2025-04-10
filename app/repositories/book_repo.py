from app import db
from app.models.book_model import Book

class BookRepository:
    
    @staticmethod
    def get_all_books():
        return Book.query.all()
    
    @staticmethod
    def get_book_by_id(book_id):
        return Book.query.get(book_id)
    
    @staticmethod
    def add_book(book_data):
        book = Book(
            title=book_data['title'],
            description=book_data['description'],
            category_id=book_data['category_id'],
            author_id=book_data['author_id'],
            published=book_data['published'],
            quantity=book_data['quantity'],
            file=book_data['file'],
            cover_image_path=book_data['cover_image_path'],
            full_pay_price=book_data['full_pay_price'],
            rent_price=book_data['rent_price'],
        )
        db.session.add(book)
        db.session.commit()

    @staticmethod
    def update_book(book_id, book_data):
        book = Book.query.get(book_id)
        if book:
            book.title = book_data['title']
            book.description = book_data['description']
            book.category_id = book_data['category_id']
            book.author_id = book_data['author_id']
            book.published = book_data['published']
            book.cover_image_path=book_data['cover_image_path']
            book.quantity = book_data['quantity']
            book.file = book_data['file']
            book.full_pay_price = book_data['full_pay_price']
            book.rent_price = book_data['rent_price']
            db.session.commit()

    @staticmethod
    def delete_book(book_id):
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()

    @staticmethod
    def get_books_litmited_by_six():
        return Book.query.limit(6).all()
    
    @staticmethod
    def get_books_offset_limit(offset, limit):
        return Book.query.offset(offset).limit(limit).all()