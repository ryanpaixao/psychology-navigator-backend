from database import Base, engine
from models import Paper, Citation

# Just test if models can be loaded
print("Models loaded successfully!")

try:
    connection = engine.connect()
    print("Database connection successful!")
    connection.close()
except Exception as e:
    print(f"Database connection failed: {e}")