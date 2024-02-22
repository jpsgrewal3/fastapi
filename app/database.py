from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg
from psycopg import ClientCursor
import time
from .config import settings


# SQLAlchemy specific code, as with any other app
DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# while True:
#     try:
#         conn = psycopg.connect(host='localhost', dbname='fastapi', user='postgres',
#                             password='Bunnygrewal222', cursor_factory=ClientCursor)
#         cursor = conn.cursor()
#         print ("DB Connection successful!")
#         break
#     except Exception as error:
#         print("Conn to DB failed!")
#         print("Error:", error)
#         time.sleep(3)