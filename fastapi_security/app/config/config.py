import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
ALGORITHM = os.getenv('ALGORITHM')
DATABASE_URL = "mysql+pymysql://"+os.getenv('DB_HOST')+":"+os.getenv('DB_PASSWORD')+"@"+os.getenv('DB_DOMAIN')+"/"+ os.getenv('DB_SCHEMA')
