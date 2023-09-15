from core.database import db
from models.Movie import Movie

def fetchMovies():
    result = db.query(Movie).all()
    return [r.to_dict() for r in result]