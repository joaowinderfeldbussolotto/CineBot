from datetime import datetime,timedelta
from core.database import db
from models.Session import Session

def fetchSessionByDay(days_ahead):
  """
   Fetch sessions by day. This is used to determine which sessions are in the past and which aren't
   
   @param days_ahead - Number of days ahead to fetch
   
   @return A list of Session objects in chronological order
  """
  start_date = datetime.now()
  end_date = start_date + timedelta(days=days_ahead)
  results = db.query(Session).filter(Session.begin >= start_date, Session.begin < end_date).all()

  return results

def update_seats_session(number_of_seats, session_id):
    session = db.query(Session).filter(Session.id == session_id).first()
    if session is None:
      return False
    db.begin()
    session.avaliable_seats += number_of_seats
    db.commit()
    db.close()
    return True

def cancel_seats(number_of_seats, session_id):
  return update_seats_session(number_of_seats, session_id)

def reserve_seats(number_of_seats, session_id):
   return update_seats_session(-1*number_of_seats, session_id)

def fetchAvailableCinemaSeat(session_id, seats):
  result = db.query(Session).filter(Session.id == session_id, Session.avaliable_seats > seats).first()
  return result 