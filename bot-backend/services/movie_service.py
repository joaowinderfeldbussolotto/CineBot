from core.database import db
from models.Movie import Movie

def fetchMovies():
    """
     Fetches movies from the database.
     
     
     @return A list of dictionaries containing movie information.
    """
    result = db.query(Movie).all()
    return [r.to_dict() for r in result]