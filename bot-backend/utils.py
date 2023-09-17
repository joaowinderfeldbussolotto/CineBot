import json
from datetime import datetime

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
      "filme": result.movie.title,
      "sala": result.room.name,
      "inicio": datetime_serializer(result.begin),
      "fim": datetime_serializer(result.end),
      "preco": float(result.price)
    }
    sessions_as_dict.append(session_dict)
  return {"sessoes": sessions_as_dict}