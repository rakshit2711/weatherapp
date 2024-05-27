from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
DATABASE_URL = "postgresql://weather_owner:Xig2jZdD0ehw@ep-holy-wave-a1k2vm0b.ap-southeast-1.aws.neon.tech/weather?sslmode=require"
db = None
def get_db():
    global db
      # Update with your credentials
    if db == None:
        engine = create_engine(DATABASE_URL)

        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
    return db