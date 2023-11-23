from dotenv import load_dotenv
import os
load_dotenv()

class Settings:
    RDS_DATABASE_URI = os.environ.get('DB_URI')
    EMAIL_SENDER = os.environ.get('EMAIL_SENDER')
    EMAIL_APP_PASSWORD = os.environ.get('EMAIL_APP_PASSWORD')

settings = Settings()
