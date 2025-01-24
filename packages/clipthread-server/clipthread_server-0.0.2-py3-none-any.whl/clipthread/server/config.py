import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "./clipboard.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    DEBUG = os.getenv("DEBUG", "false").lower() in ("true", "1", "t", "y", "yes")