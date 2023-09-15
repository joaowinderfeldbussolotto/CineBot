import json
import requests
from config import settings
from utils import prepareResponse

def get_movies(event, context):
    api_url = f"{settings.API_URL}/movie"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            movies = response.json()
            
            formatted_movies = ["Filmes em cartaz:\n"]
            for movie in movies:
                formatted_movie = (
                    f"Título: {movie['title']}\n"
                    f"Gênero: {movie['genre']}\n"
                    f"Ano de lançamento: {movie['release_year']}\n"
                    f"Diretor: {movie['director']}\n"
                    "\n"
                )
                formatted_movies.append(formatted_movie)

            result_message = '\n'.join(formatted_movies)
            
        else:
            result_message = response.json()['message']
        
        return prepareResponse(event, result_message)
    
    except Exception as e:
        return f"Error making request: {str(e)}"

