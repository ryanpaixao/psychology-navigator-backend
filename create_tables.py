from database import Base, engine
from models import Paper, Citation # Import all models

def create_database():
    # This will create all tables defined in modelss
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_database()
    print("Tables created successfully!")