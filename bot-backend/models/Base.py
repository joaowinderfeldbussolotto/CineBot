from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Base(Base):
    __abstract__ = True
    def to_dict(self):
        return {field.name:getattr(self, field.name) for field in self.__table__.c}
