from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"  # Using SQLite for simplicity

# Set up the database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Function to create the database tables
def init_db():
    SQLModel.metadata.create_all(engine)


### Database Models ###


class DBModel(SQLModel, table=True):
    __tablename__ = "dbmodel"
