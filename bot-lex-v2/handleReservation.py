import json
import requests
from .config import settings

def delete_reservation(event, context):
    print(event)
    slots = event['interpretations'][0]['intent']['slots']
    email = slots['email']['value']['interpretedValue']
    reservation_id = slots['reservationID']['value']['interpretedValue']
    
    api_url = settings.API_URL

    params = {
        "user_email": email,
        "reservation_id": reservation_id
    }
    
    try:
        response = requests.delete(api_url, params=params)

        if(response.status_code == 204):
            status = 'Fulfilled'
            result_message = 'Deletado com sucesso.'
        else:
            status = 'Failed'
            result_message = response.json()
            
        response_message = {
            "dialogAction": {
            "type": "Close"
            },
            "intent": {
                "state": status  
            },
            "messages": [
            {
                "contentType": "PlainText",
                "content": result_message 
            }
            ]
        }
        return response_message
    
    except Exception as e:
        print("Error:", e)
        return {
            "statusCode": 500,
            "body": "An error occurred while processing your request."
        }
