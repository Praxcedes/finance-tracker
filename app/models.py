from . import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    transactions = db.relationship("Transaction", backref="user", lazy=True)
    categories = db.relationship("Category", backref="user", lazy=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(7), default="#16a34a")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    transactions = db.relationship("Transaction", backref="category", lazy=True)
