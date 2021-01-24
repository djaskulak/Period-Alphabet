from dotenv import load_dotenv
import os

load_dotenv()

DB_CREDENTIALS = os.getenv("DB_CREDENTIALS")
