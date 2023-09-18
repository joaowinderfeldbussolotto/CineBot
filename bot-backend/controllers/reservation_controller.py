from utils import Response, transform_email
from services.reservation_service import fetchReservations, fetchReservationByIdAndEmail, deleteReservation
from http_exceptions import NotFoundException, InternalServerErrorException, HTTPException, BadRequestException
from services.email_service import send_email

def getQueryParameters(event):
    """
     Extracts query parameters from event. This is used to extract user_email and reservation_id from query parameters.
     
     @param event - Event which contains query parameters.
     
     @return Tuple of ( user_email reservation_id)
    """
    query_params = event.get('queryStringParameters')
    if query_params:
        user_email, reservation_id = query_params.get('user_email', ''), query_params.get('reservation_id', '')
        if not (user_email and reservation_id):
            raise BadRequestException('Por favor, informe os campos: user_email e reservation_id')
        return transform_email(user_email), reservation_id
    
def get_reservations(event, context):
    try:       
        reservations = fetchReservations()
        if (reservations):
            response = Response(200, reservations)
        else:
            response = Response(204)
    
    except HTTPException as http_exception:
        return Response(http_exception.status_code, {"message":http_exception.message})
    except Exception as e:
        return Response(500, {"message": str(e)})

    return response

def delete_reservation(event, context):
    try:     
        user_email, reservation_id = getQueryParameters(event)
        reservation = fetchReservationByIdAndEmail(user_email, reservation_id)
        if (reservation):
            reservation_dict = reservation.to_dict()
            deleteReservation(reservation)
            send_email(reservation_dict, 'Cancelamento')
            return Response(204)
        
        raise NotFoundException("Não foi encontrado reservas para esse email e ID.")
        
    except HTTPException as http_exception:
        return Response(http_exception.status_code, body={"message":http_exception.message})
    
    except Exception as e:
        return Response(500, {"message": str(e)})
