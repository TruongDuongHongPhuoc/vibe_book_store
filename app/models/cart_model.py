from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db

class Cart(db.Model):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price_per_unit = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    rent_or_purchase = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    book = db.relationship('Book', backref='carts')

    reader_id = db.Column(db.Integer, db.ForeignKey('reader.id'), nullable=False)
    reader = db.relationship('Reader', backref='carts')

    def __init__(self, quantity, price_per_unit, rent_or_purchase, book_id, reader_id):
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.total_price = price_per_unit * quantity
        self.rent_or_purchase = rent_or_purchase
        self.book_id = book_id
        self.reader_id = reader_id


