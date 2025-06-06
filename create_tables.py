from database import Base, engine
from models import Paper, Citation # Import all models
from sqlalchemy import inspect # For verification

def verify_tables():
    inspector = inspect(engine)
    print("Existing tables:", inspector.get_table_names())

def create_database():
    # This will create all tables defined in modelss
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")


if __name__ == "__main__":
    verify_tables()
    create_database()
    verify_tables()