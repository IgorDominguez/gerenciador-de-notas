from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URL = "sqlite:///db/notes.db"

db = create_engine(DB_URL)

Session = sessionmaker(bind=db)
Base = declarative_base()