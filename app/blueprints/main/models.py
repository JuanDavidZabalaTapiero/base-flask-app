from app.extensions import db

class Main(db.Model):
    __tablename__ = "main"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)