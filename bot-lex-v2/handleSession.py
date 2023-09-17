from config import settings
import requests
import json
from utils import prepareResponse, format_sessions


def fetch_session_data(day):
    api_url = f"{settings.API_URL}/session"
    data = {"dayForSearch": day}
    headers = {"Content-Type": "application/json"}

    response = requests.post(api_url, data=json.dumps(data), headers=headers)

    if response.status_code != 200:
        raise Exception(f"Erro na solicitação à API: {response.status_code}")
    
    return response.json()

def getSessionsByDay(event, context):
    try:
        slots = event['sessionState']['intent']['slots']
        days = slots['day']['value']['interpretedValue']

        if not days:
          raise ValueError("O valor 'dia' não foi fornecido ou não está no formato esperado.")
        
        json_data = fetch_session_data(int(days))
        result_message = format_sessions(json_data.get("sessoes", []))

        return prepareResponse(event, result_message)

    except Exception as e:
        print("Error:", str(e))
        return prepareResponse(event, "Ocorreu um erro!")
