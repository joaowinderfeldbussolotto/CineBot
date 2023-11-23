import os

class Settings:
    API_URL = os.environ.get('API_URL')

settings = Settings()
