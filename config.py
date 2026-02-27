import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    URL = os.getenv("URL")
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")

config = Config()