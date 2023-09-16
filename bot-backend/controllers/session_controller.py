
import json
from utils import Response, format_session_list
from services.session_service import fetchSessionByDay


    
def getSessionsByDays(event, context):
    try:
        request_data = json.loads(event['body'])
        if 'dayForSearch' in request_data and isinstance(request_data['dayForSearch'], int) and request_data['dayForSearch'] > 0:
            days_ahead = request_data['dayForSearch']
            results = fetchSessionByDay(days_ahead)
            dataList = format_session_list(results)

            return Response(200, dataList)
        else:
            return Response(400, {"error": "The 'dayForSearch' field must be an positive integer"})
    except Exception as e:
        return Response(500, {"error": str(e)})
