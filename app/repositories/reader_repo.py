from app import db
from app.models.reader_model import Reader

class ReaderRepository:
    def __init__(self):
        self.model = Reader

    def get_all_readers(self):
        return self.model.query.all()

    def get_reader_by_id(self, reader_id):
        return self.model.query.get(reader_id)

    def add_reader(self, data):
        reader = self.model(**data)
        db.session.add(reader)
        db.session.commit()
        return reader

    def update_reader(self, reader_id, data):
        reader = self.model.query.get(reader_id)
        if reader:
            for key, value in data.items():
                setattr(reader, key, value)
            db.session.commit()
        return reader

    def delete_reader(self, reader_id):
        reader = self.model.query.get(reader_id)
        if reader:
            db.session.delete(reader)
            db.session.commit()
        return reader
