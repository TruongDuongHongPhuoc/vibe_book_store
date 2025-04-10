from datetime import datetime
from app import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String(255), nullable=True)  # Image for the book
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('reader.id'), nullable=False)
    published = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cover_image_path = db.Column(db.String(255), nullable=False)
    file = db.Column(db.String(255), nullable=True)  # File after purchase (e.g., eBook file)
    full_pay_price = db.Column(db.Float, nullable=False)
    rent_price = db.Column(db.Float, nullable=False)

    # Relationships
    category = db.relationship('Category', backref='books')
    author = db.relationship('Reader', backref='books')
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description[:100],
            "cover_image_path": self.cover_image_path,
            "author": self.author.full_name if self.author else "Unknown",
            "full_pay_price": self.full_pay_price,
        }
    def __repr__(self):
        return f'<Book {self.title}>'
    
     
    
