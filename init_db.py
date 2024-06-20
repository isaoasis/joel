from page import db, app

def initialize_database():
    with app.app_context():
        try:
            db.create_all()
            print("Database tables created.")
        except Exception as e:
            print(f"Error creating database tables: {e}")

if __name__ == "__main__":
    initialize_database()
