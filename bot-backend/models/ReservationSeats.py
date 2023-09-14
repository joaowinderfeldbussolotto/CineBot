from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.Base import Base
from models.Seat import Seat
from models.Reservation import Reservation

class ReservationSeats(Base):
    __tablename__ = 'reservas_poltronas'

    id = Column(Integer, primary_key=True)
    reservation_id = Column("id_reserva", ForeignKey('reservas.id'), nullable=False, index=True)
    seat_id = Column("id_poltrona", ForeignKey('poltronas.id'), nullable=False, index=True)

    poltrona = relationship('Seat')
    reserva = relationship('Reservation')
