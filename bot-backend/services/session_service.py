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