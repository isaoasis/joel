from page import app, db

def initialize_database():
    try:
        with app.app_context():
            db.create_all()
        print("Database tables created.")
    except Exception as e:
        print(f"Error creating database tables: {e}")

if __name__ == "__main__":
    initialize_database()
