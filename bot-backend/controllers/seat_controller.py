import json
from services.seat_service import fetchAvailableCinemaSeat
from utils import Response, format_available_seats

def get_available_seats(event, context):
    try:
        print(event)
        request_data = json.loads(event['body'])
        print(request_data['session_id'])
        if 'session_id' in request_data:
            session_id = request_data['session_id']
            print('estou aqui 1 ')
            result = fetchAvailableCinemaSeat(session_id)
            print(f'resultado: {result}')
            data = format_available_seats(result)
            print(f'data: {data}')
            return Response(200, data)
        else:
            return Response(400, {"error": "A sessão que está buscando não está disponível"})
    except Exception as e:
        return Response(500, {"error": str(e)})