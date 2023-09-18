from sqlalchemy.sql import text
from core.database import engine

def fetchAvailableCinemaSeat(session_id):
    q = f"select * from poltronas p where id_sala = (select id_sala from sessoes where id = ${session_id} and data_hora_fim >= now()) and id not in (select id_poltrona from reservas_poltronas rp where id_reserva in (select id from reservas r where id_sessao = ${session_id}))"
    query = text(q)
    result = engine.connect().execute(query)
    return [dict(row) for row in result]
