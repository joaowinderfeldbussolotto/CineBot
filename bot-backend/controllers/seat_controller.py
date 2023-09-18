import json
from services.seat_service import fetchAvailableCinemaSeat
from utils import Response

def get_available_seats(event, context):
    try:
        request_data = json.loads(event['body'])
        if 'session_id' in request_data:
            result = fetchAvailableCinemaSeat(request_data['session_id'])
            return Response(200, result)
        else:
            return Response(400, {"error": "A sessão que está busando não está disponível"})
    except Exception as e:
        return Response(500, {"error": str(e)})