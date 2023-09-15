import json
import requests
from config import settings
from utils import prepareResponse


def delete_reservation(event, context):
    print(event)
    slots = event['interpretations'][0]['intent']['slots']
    email = slots['email']['value']['interpretedValue']
    reservation_id = slots['ReservationID']['value']['interpretedValue']
    
    api_url = f"{settings.API_URL}/reservation"

    params = {
        "user_email": email,
        "reservation_id": reservation_id
    }
    
    try:
        response = requests.delete(api_url, params=params)
        if(response.status_code == 204):
            result_message = 'Deletado com sucesso.'
        else:
            result_message = response.json()['message']
        return prepareResponse(event, result_message)
    
    except Exception as e:
        print("Error:", e)
        return {
            "statusCode": 500,
            "body": "An error occurred while processing your request."
        }
