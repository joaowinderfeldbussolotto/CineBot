import json
import random
from utils import createResponseData

def get_reservation(event, context):
    try:
        query_params = event.get('queryStringParameters')
        user_email = ''
        reservation_id = ''
        if query_params is not None:
            user_email = query_params.get('user_email', '')
            reservation_id = query_params.get('reservation_id', '')

        reservation_exists = random.randint(1,2) == 1
        if (reservation_exists):
            response = createResponseData(200, json.dumps({"message": "Reservation exists"}))
        else:
            response = createResponseData(404, json.dumps({"message": "Reservation not found"}))
    except Exception as e:
        return createResponseData(500, json.dumps({"message": str(e)}))

    return response
