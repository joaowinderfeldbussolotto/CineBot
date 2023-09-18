import json
from datetime import datetime
import re
import hashlib

def transform_email(text):
    """
     Extracts and returns the email address from the text.
     
     @param text - The text to be parsed
     
     @return The email address if found 
    """
    match = re.search(r'<mailto:(.*?)\|.*?>', text)

    if match:
        email = match.group(1)
        return email
    else:
        return text



def Response(statusCode, body=''):
    """
     Create a response with the given status code and body
     
     @param statusCode - The status code to return
     @param body - The body of the response. Defaults to a blank string
     
     @return A dictionary that can be sent as response
    """
    return {
        'statusCode': statusCode,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        },
        'body': json.dumps(body)
    }
def datetime_serializer(obj):
    """
     Serialize datetime to string. This is used to make sure we don't accidentally get datetime.
     
     @param obj - Object to be serialized.
     
     @return String representation of datetime or None if obj is not a datetime object ( for example in case of error
    """
    if isinstance(obj, datetime):
        return obj.strftime("%d/%m/%Y %H:%M")

def format_session_list(results):
  """
   Formats a list of sessions into a list of dictionaries. This is used to create JSON objects
   
   @param results - A list of Session objects
   
   @return A list of dictionaries
  """
  sessions_as_dict = []

  for result in results:
    session_dict = {
      "id": result.id,
      "filme": result.movie.title,
      "sala": result.room.name,
      "inicio": datetime_serializer(result.begin),
      "fim": datetime_serializer(result.end),
      "preco": float(result.price)
    }
    sessions_as_dict.append(session_dict)
  return {"sessoes": sessions_as_dict}

def format_available_seats(results):
  """
   Format seats to dict.
   
   @param results - list of dictionaries returned by search function
   
   @return dict
  """
  seats_as_dict = []
  print('estou no util')
  print(f'dict ?? : {results[0]}')
  print(f"tipo: {type(results[0])}")
  
  for result in results:
    result = list(result.values())
    seat_dict = {
      "id": int(result[0]),
      "id_sala": int(result[1]),
      "fileira": result[2],
      "numero": int(result[3])
    }
    seats_as_dict.append(seat_dict)
  
  print(seats_as_dict)
  
  return {"poltronas": seats_as_dict}

def get_hash(username, time):
  try:
    h = hashlib.new('sha256', usedforsecurity=True)
    h.update(username.encode("utf-8"))
    h.update(str(time).encode("utf-8"))
    return h.hexdigest()
  except:
    raise Exception('Cannot generate hash')