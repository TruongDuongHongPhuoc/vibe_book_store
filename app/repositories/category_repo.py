from app.models.category_model import Category
from app import db

class CategoryRepository:
    def get_all_categories(self):
        return Category.query.all()

    def get_category_by_id(self, id):
        return Category.query.get(id)

    def add_category(self, data):
        category = Category(name=data['name'])
        db.session.add(category)
        db.session.commit()

    def update_category(self, id, data):
        category = Category.query.get(id)
        if category:
            category.name = data['name']
            db.session.commit()

    def delete_category(self, id):
        category = Category.query.get(id)
        if category:
            db.session.delete(category)
            db.session.commit()
