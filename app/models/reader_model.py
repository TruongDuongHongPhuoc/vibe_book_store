from app import db

class Reader(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.Date, nullable=True)
    gmail = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.Boolean, nullable=False)  # True for male, False for female
    nation = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Integer, nullable=False, default=1)  # 1: user, 2: writer, 3: admin, 4 : blocked

    def __repr__(self):
        return f"<Reader {self.full_name} - Role: {self.role}>"
