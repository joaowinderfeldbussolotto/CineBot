from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.Base import Base
from models.Session import Session

class Reservation(Base):
    __tablename__ = 'reservas'

    id = Column(Integer, primary_key=True)
    session_id = Column("id_sessao", ForeignKey('sessoes.id'), nullable=False, index=True)
    user_name = Column("nome_usuario", String(255), nullable=False)
    user_email = Column("email_usuario", String(255), nullable=False)
    create_time = Column("create_time", DateTime, nullable=False)

    session = relationship('Session')
