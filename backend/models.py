from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # max 80 chars, unique, required
    username = db.Column(db.String(80), unique=True, nullable=False)
    # max 120 chars, unique, required
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    tasks = db.relationship("Task", backref="owner", lazy=True)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)  # Text = longer strings
    status = db.Column(db.String(20), default="pending")  # pending, completed, overdue
    # Foreign key - connects this task to a user
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
