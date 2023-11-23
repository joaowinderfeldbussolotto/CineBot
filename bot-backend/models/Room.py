from sqlalchemy import Column, Integer, String
from models.Base import Base


class Room(Base):
    __tablename__ = 'salas'

    id = Column(Integer, primary_key=True)
    name = Column("nome", String(45), nullable=False)