from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL Connection Details
MYSQL_USER = "bssuser"
MYSQL_PASSWORD = "bssuser@123"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DB = "employee_db"

DATABASE_URL = "mysql+pymysql://bssuser:Bssuser%40123@localhost:3306/employee_db"

# DATABASE_URL = r"mysql+pymysql://bssuser:Bssuser@123@localhost:3306/employee_db" r used for raw format of the string
# r before a string makes it a raw string, meaning backslashes (\) are treated as literal characters instead of escape sequences.

# Create Engine
engine = create_engine(DATABASE_URL)

# Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base Class for ORM Models
Base = declarative_base()
