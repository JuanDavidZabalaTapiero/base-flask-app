from app.extensions import db


class UserTest(db.Model):
    __tablename__ = "user_test"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
