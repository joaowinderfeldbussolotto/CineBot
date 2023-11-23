from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_serializer import SerializerMixin


Base = declarative_base()

class Base(Base, SerializerMixin):
    __abstract__ = True

