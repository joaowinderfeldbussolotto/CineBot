from dotenv import load_dotenv
import os
load_dotenv()

class Settings:
    RDS_DATABASE_URI = os.environ.get('DB_URI')

settings = Settings()
