

def prepareResponse(event, msgText):
  """
   Prepares a response to be sent to Amazon lex
   
   @param event - The event that triggered the close intent
   @param msgText - The message text to send to Amazon lex
   
   @return A dictionary that can be sent to Amazon lex with the close intent and the message text as
  """
  response = {
          "sessionState": {
            "dialogAction": {
              "type": "Close"
            },
            "intent": {
              "name": event['sessionState']['intent']['name'],
              "slots": event['sessionState']['intent']['slots'],
              "state": "Fulfilled"
            }
          },
          "messages": [
            {
              "contentType": "PlainText",
              "content": msgText
            }
            ]
        }
      
  return response

def format_sessions(sessions):
    """
     Formats sessions for display. This is a helper function to format the sessions in a human readable format.
     
     @param sessions - A list of dictionaries containing session information.
     
     @return A nicely formatted string containing the sessions in the human format returned`
    """
    formatted_sessions = ["Sessões disponíveis:\n"]

    for session in sessions:
        formatted_session = (
            f"Id: {session['id']},\n"
            f"Filme: {session['filme']},\n"
            f"Sala: {session['sala']},\n"
            f"Início: {session['inicio']},\n"
            f"Fim: {session['fim']},\n"
            f"Preço: {session['preco']},\n"
        )
        formatted_sessions.append(formatted_session)

    return '\n'.join(formatted_sessions)

