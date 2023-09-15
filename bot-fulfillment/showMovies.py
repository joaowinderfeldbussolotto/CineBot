from utils import prepareResponse

def lambda_handler(event):
    msgText = "Deu certoooooo!!!!"
    return prepareResponse(event, msgText)