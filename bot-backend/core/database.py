from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings

engine = create_engine(settings.RDS_DATABASE_URI)
Session = sessionmaker(autocommit = True, bind = engine)
db = Session()
