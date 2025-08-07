from flask import Flask, jsonify, request
from models import db, User, Task
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///taskmanager.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Connect database to app
db.init_app(app)

# Create db tables when app starts
with app.app_context():
    db.create_all()


@app.route("/test-db")
def test_database():
    try:
        # Try to query the User table (even if it's empty)
        user_count = User.query.count()
        task_count = Task.query.count()

        return jsonify(
            {
                "database_status": "connected",
                "users": user_count,
                "tasks": task_count,
                "message": "Database is working perfectly",
            }
        )
    except Exception as e:
        return jsonify({"database_status": "error", "message": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
