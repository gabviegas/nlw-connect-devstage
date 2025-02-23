from flask import Blueprint, jsonify, request

# Cria um agregador de rotas relacionadas a eventos
events_link_route_bp = Blueprint("events_link_route", __name__)

# Interação com html
from src.http_types.http_request import httpRequest

# Repositório associado
from src.model.repositories.eventos_link_repository import EventosLinkRepository

# Criador de links de eventos
from src.controllers.events_link.events_link_creator import EventsLinkCreator

# Cria uma rota "events_link" com o método POST
@events_link_route_bp.route("/events_link", methods=["POST"])
def create_new_link():
    events_link_repo = EventosLinkRepository()
    events_link_creator = EventsLinkCreator(events_link_repo) # lógica de criação de eventos

    http_request = httpRequest(body=request.json) # seleciona o body do request do html

    http_response = events_link_creator.create(http_request) # execução da lógica de criação

    return jsonify(http_response.body), http_response.status_code # retornando uma informação para o usuário