from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings

engine = create_engine(settings.RDS_DATABASE_URI)
Session = sessionmaker(bind=engine)
db = Session()
