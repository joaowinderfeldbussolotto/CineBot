from utils import Response
from services.reservation_service import fetchReservations, fetchReservationByIdAndEmail, deleteReservation
from http_exceptions import NotFoundException, InternalServerErrorException, HTTPException, BadRequestException

def getQueryParameters(event):
    query_params = event.get('queryStringParameters')
    if query_params:
        user_email, reservation_id = query_params.get('user_email', ''), query_params.get('reservation_id', '')
        if not (user_email and reservation_id):
            raise BadRequestException('Por favor, informe os campos: user_email e reservation_id')
        return user_email, reservation_id
    
def get_reservations(event, context):
    try:       
        reservations = fetchReservations()
        if (reservations):
            response = Response(200, reservations)
        else:
            raise NotFoundException
    
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
            deleteReservation(reservation)
            # message = f"The reservation with id {reservation.id} was cancelled."
            return Response(204)
        
        raise NotFoundException("Não foi encontrado reservas para esse email e ID.")
        
    except HTTPException as http_exception:
        return Response(http_exception.status_code, body={"message":http_exception.message})
    
    except Exception as e:
        return Response(500, {"message": str(e)})


