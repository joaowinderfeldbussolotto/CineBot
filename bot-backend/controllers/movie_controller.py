from utils import Response
from services.movie_service import fetchMovies
from http_exceptions import NotFoundException, InternalServerErrorException, HTTPException

def get_movies(event, context):
    try:       
        movies = fetchMovies()
        if (movies):
            response = Response(200, movies)
        else:
            raise NotFoundException
    
    except HTTPException as http_exception:
        return Response(http_exception.status_code, {"message":http_exception.message})
    except Exception as e:
        return Response(500, {"message": str(e)})

    return response



