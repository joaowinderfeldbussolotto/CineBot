import json
import requests
from config import settings
from utils import prepareResponse
from datetime import datetime

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
    
def create_reservation(event, context):
    try:
        slots = event['sessionState']['intent']['slots']
        session_id = slots['sessionID']['value']['interpretedValue']
        qt_reservations = slots['qtReservation']['value']['interpretedValue']
        user_mail = slots['mail']['value']['interpretedValue']
        user_name = slots['name']['value']['interpretedValue']
        number_of_seats = slots['qtReservation']['value']['interpretedValue']
        print(f'josue{event}')
        avaliable_seats = fetch_reservation_data(session_id, number_of_seats)
        print(f"joao{avaliable_seats}")

        if int(avaliable_seats['avaliable_seats']) > 0:
            api_url = f"{settings.API_URL}/reservation"
            data = {
                "id_sessao": session_id,
                "nome_usuario": user_name,
                "email_usuario": user_mail,
                "quantidade_poltronas": int(number_of_seats)
            }
            print(f'data ::: {data}')
            headers = {"Content-Type": "application/json"}
            
            response = requests.post(api_url, data=json.dumps(data), headers=headers)
            if(response.status_code == 204):
                result_message = 'Inserido com sucesso.'
            else:
                result_message = response.json()['message']
            return prepareResponse(event, result_message)
            
    except Exception as e:
        print("Error:", str(e))
        return prepareResponse(event, "Infelizmente esta sessão não está mais disponível.")

def fetch_reservation_data(session_id, num_of_seats):
    
    api_url = f"{settings.API_URL}/get_seats"
    data = {"id_sessao": session_id, "num_of_seats": num_of_seats}
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(api_url, data=json.dumps(data), headers=headers)

    if response.status_code != 200:
        raise Exception(f"Erro na solicitação à API: {response.status_code}")
    
    return response.json()
