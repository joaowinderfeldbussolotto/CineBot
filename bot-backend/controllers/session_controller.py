
import json
from utils import Response, format_session_list, format_available_seats
from services.session_service import fetchSessionByDay, fetchAvailableCinemaSeat

def getSessionsByDays(event, context):
    try:
        request_data = json.loads(event['body'])
        if 'dayForSearch' in request_data and isinstance(request_data['dayForSearch'], int) and request_data['dayForSearch'] > 0:
            days_ahead = request_data['dayForSearch']
            results = fetchSessionByDay(days_ahead)
            dataList = format_session_list(results)
            return Response(200, dataList)
        else:
            return Response(400, {"error": "O campo 'dayForSearch' deve ser um inteiro positivo"})
    except Exception as e:
        return Response(500, {"error": str(e)})

def get_available_seats(event, context):
    try:
        request_data = json.loads(event['body'])
        if 'id_sessao' and 'num_of_seats' in request_data:
            session_id = request_data['id_sessao']
            num_of_seats = request_data['num_of_seats']
            result = fetchAvailableCinemaSeat(session_id,num_of_seats)
            result = result.to_dict()
            return Response(200, result)
        else:
            return Response(400, {"error": "A sessão que está buscando não está disponível"})
    except Exception as e:
        return Response(500, {"error": str(e)})