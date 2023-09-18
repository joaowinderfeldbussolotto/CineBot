from core.database import db
from models.Reservation import Reservation


def fetchReservationByIdAndEmail(user_email, reservation_id):
    result = db.query(Reservation).filter(Reservation.user_email == user_email, Reservation.id == reservation_id).first()
    return result

def fetchReservations():
    result = db.query(Reservation).all()
    return [r.to_dict() for r in result]

def deleteReservation(reservation: Reservation):
    db.begin()
    db.delete(reservation)
    db.commit()
    db.close()
