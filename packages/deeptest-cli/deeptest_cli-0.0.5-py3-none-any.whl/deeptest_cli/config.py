import os

from dotenv import load_dotenv

load_dotenv(override=True)


class Config:
    BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")
