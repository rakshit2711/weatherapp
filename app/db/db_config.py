from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
DATABASE_URL = "postgresql://rakshit:rak@127.0.0.2:5432/weather"
db = None
def get_db():
    global db
      # Update with your credentials
    if db == None:
        engine = create_engine(DATABASE_URL)

        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
    return db