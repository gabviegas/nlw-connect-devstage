from flask import Blueprint, jsonify, request

# Cria um agregador de rotas relacionadas a eventos
subs_route_bp = Blueprint("subs_route", __name__)

# Validador
from src.validators.subscribers_creator_validator import subscribers_creator_validator

# Interação com html
from src.http_types.http_request import httpRequest

# Criador de eventos
from src.controllers.subscribers.subscribers_creator import SubscribersCreator
from src.model.repositories.subscribers_repository import SubscribersRepository

# Cria uma rota "event" com o método POST
@subs_route_bp.route("/subscriber", methods=["POST"])
def create_new_subscriber():
    subscribers_creator_validator(request) # valida o request do html
    http_request = httpRequest(body=request.json) # seleciona o body do request do html

    subs_repo = SubscribersRepository() # lógica de criação de eventos
    subs_creator = SubscribersCreator(subs_repo) 

    http_response = subs_creator.create(http_request) # execução da lógica de criação
    
    return jsonify(http_response.body), http_response.status_code # retornando uma informação para o usuário