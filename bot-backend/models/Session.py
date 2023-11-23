from sqlalchemy import Column, DECIMAL, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.Base import Base
from models.Movie import Movie
from models.Room import Room


class Session(Base):
    __tablename__ = 'sessoes'

    id = Column(Integer, primary_key=True)
    id_filme = Column("id_filme", ForeignKey('filmes.id'), nullable=False, index=True)
    begin = Column("data_hora_inicio", DateTime, nullable=False)
    end = Column("data_hora_fim", DateTime, nullable=False)
    room_id = Column("id_sala", ForeignKey('salas.id'), nullable=False, index=True)
    price = Column("preco", DECIMAL(8, 2), nullable=False)
    avaliable_seats = Column("poltronas_disponiveis", Integer, nullable=False)

    movie = relationship('Movie')
    room = relationship('Room')
