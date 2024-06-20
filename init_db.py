# init_db.py
from page import db, app

with app.app_context():
    db.create_all()
    print("Database tables created.")
