from .db import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def __init__(self, username, name, password):
        self.name = name
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"