from utils import prepareResponse

def lambda_handler(event, context):
    msgText = "Deu certoooooo!!!!"
    return prepareResponse(event, msgText)