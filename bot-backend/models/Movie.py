from sqlalchemy import Column, Integer, String
from models.Base import Base

class Movie(Base):
    __tablename__ = 'filmes'

    id = Column(Integer, primary_key=True)
    title = Column("titulo", String(255), unique=True, nullable=False)
    genre = Column("genero",String(45), nullable=False)
    director = Column("diretor", String(45), nullable=False)
    release_year = Column("ano_lancamento", Integer(), nullable=False)

