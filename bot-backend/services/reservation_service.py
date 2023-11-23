from core.database import db
from models.Reservation import Reservation


def fetchReservationByIdAndEmail(user_email, reservation_id):
    """
     Fetch a reservation by id and user email. This is used to check if there is a reservations with the same user email and id
     
     @param user_email - Email of the user who owns the reservation
     @param reservation_id - ID of the reservation to look up
     
     @return The reservation or None if not found or no reservation
    """
    result = db.query(Reservation).filter(Reservation.user_email == user_email, Reservation.id == reservation_id).first()
    return result

def fetchReservations():
    """
     Fetch reservations from the database. This is used to populate the list of reservations that are in the database
     
     
     @return A list of dicts with the
    """
    result = db.query(Reservation).all()
    return [r.to_dict() for r in result]

def deleteReservation(reservation: Reservation):
    """
     Delete a reservation from the database. This is a destructive operation. If you want to delete a reservation that is in the process of being reclaimed use
     
     @param reservation - The reservation to delete
    """
    db.begin()
    db.delete(reservation)
    db.commit()
    db.close()

def insertReservation(reservation: Reservation):
    db.begin()
    db.add(reservation)
    db.commit()
    db.close()
