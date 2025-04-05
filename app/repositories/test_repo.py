from app import db
from app.models.test import Test

class TestRepository:
    def __init__(self):
        self.model = Test

    def get_all_tests(self):
        return self.model.query.all()

    def get_test_by_id(self, test_id):
        return self.model.query.get(test_id)

    def add_test(self, data):
        test = self.model(**data)
        db.session.add(test)
        db.session.commit()
        return test

    def update_test(self, test_id, data):
        test = self.get_test_by_id(test_id)
        if test:
            for key, value in data.items():
                setattr(test, key, value)
            db.session.commit()
        return test

    def delete_test(self, test_id):
        test = self.get_test_by_id(test_id)
        if test:
            db.session.delete(test)
            db.session.commit()
        return test
