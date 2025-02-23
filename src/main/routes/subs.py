from flask import Blueprint, jsonify, request

# Cria um agregador de rotas relacionadas a eventos
subs_route_bp = Blueprint("subs_route", __name__)

# Validador
from src.validators.subscribers_creator_validator import subscribers_creator_validator

# Interação com html
from src.http_types.http_request import httpRequest

#Repositório
from src.model.repositories.subscribers_repository import SubscribersRepository

# Criador e gerenciador de inscritos
from src.controllers.subscribers.subscribers_creator import SubscribersCreator
from src.controllers.subscribers.subscribers_manager import SubscriberManager


# Cria uma rota "subscriber" com o método POST
@subs_route_bp.route("/subscriber", methods=["POST"])
def create_new_subscriber():
    subscribers_creator_validator(request) # valida o request do http
    http_request = httpRequest(body=request.json) # seleciona o body do request do http

    subs_repo = SubscribersRepository() # lógica de criação de inscritos
    subs_creator = SubscribersCreator(subs_repo) 

    http_response = subs_creator.create(http_request) # execução da lógica de criação
    
    return jsonify(http_response.body), http_response.status_code # retornando uma informação para o usuário

# Cria uma rota dentro de "subscriber" para conseguir o link deles com o método GET
@subs_route_bp.route("/subscriber/link/<link>/event/<event_id>", methods=["GET"])
def subscribers_by_link(link, event_id):
    subs_repo = SubscribersRepository() # lógica de criação de inscritos
    subs_manager = SubscriberManager(subs_repo) 

    http_request = httpRequest(param={"link": link, "event_id": event_id}) #seleciona os parametros de url do http

    http_response = subs_manager.get_subscribers_by_link(http_request) # execução da lógica de criação
    
    return jsonify(http_response.body), http_response.status_code # retornando uma informação para o usuário

# Cria uma rota dentro de "subscriber" para fazer o ranking com o método GET
@subs_route_bp.route("/subscriber/ranking/event/<event_id>", methods=["GET"])
def link_ranking(event_id):
    subs_repo = SubscribersRepository() # lógica de criação de eventos
    subs_manager = SubscriberManager(subs_repo) 

    http_request = httpRequest(param={"event_id": event_id})

    http_response = subs_manager.get_event_ranking(http_request) # execução da lógica de criação
    
    return jsonify(http_response.body), http_response.status_code # retornando uma informação para o usuário