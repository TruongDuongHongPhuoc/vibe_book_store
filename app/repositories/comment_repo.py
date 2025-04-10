from app import db
from app.models.comment_model import Comment

class CommentRepository:
    
    @staticmethod
    def add_comment(data):
        comment = Comment(**data)
        db.session.add(comment)
        db.session.commit()
        return comment

    @staticmethod
    def get_comments_by_book(book_id):
        return Comment.query.filter_by(book_id=book_id).order_by(Comment.created_at.desc()).all()
    @staticmethod
    def delete_comment(comment_id):
        comment = Comment.query.get(comment_id)
        if comment:
            db.session.delete(comment)
            db.session.commit()
