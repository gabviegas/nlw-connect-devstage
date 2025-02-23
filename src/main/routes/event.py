from flask import Blueprint, jsonify, request

# Cria um agregador de rotas relacionadas a eventos
event_route_bp = Blueprint("event_route", __name__)

# Validador
from src.validators.events_creator_validator import events_creator_validator

# Interação com html
from src.http_types.http_request import httpRequest

# Repositório associado
from src.model.repositories.eventos_repository import EventosRepository

# Criador de eventos
from src.controllers.events.events_creator import EventsCreator

# Cria uma rota "event" com o método POST
@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
    events_creator_validator(request) # valida o request do html
    http_request = httpRequest(body=request.json) # seleciona o body do request do html

    # lógica de criação de eventos
    eventos_repo = EventosRepository() 
    events_creator = EventsCreator(eventos_repo) 

    http_response = events_creator.create(http_request) # execução da lógica de criação
    
    return jsonify(http_response.body), http_response.status_code # retornando uma informação para o usuário