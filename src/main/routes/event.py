from flask import Blueprint, jsonify, request

# Cria um agregador de rotas relacionadas a eventos
event_route_bp = Blueprint("event_route", __name__)

from src.http_types.http_response import httpResponse
from src.http_types.http_request import httpRequest

# Cria uma rota "event" com o método POST
@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
    http_request = httpRequest(body=request.json) # seleciona o body do request de .html

    http_response = httpResponse(body={ "estou" : "aqui"}, status_code=201)
    
    return jsonify(http_response.body), http_response.status_code