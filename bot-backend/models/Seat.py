from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from models.Base import Base
from models.Room import Room


class Seat(Base):
    __tablename__ = 'poltronas'

    id = Column(Integer, primary_key=True)
    room_id = Column("id_sala", ForeignKey('salas.id'), nullable=False, index=True)
    row = Column("fileira", String(1), nullable=False)
    column = Column("numero", INTEGER, nullable=False)

    sala = relationship('Room')