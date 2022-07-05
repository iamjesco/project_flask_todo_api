from app import db
from datetime import datetime


class Todos(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(250), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
