from flask import Blueprint, jsonify

# Cria um agregador de rotas relacionadas a eventos
event_route_bp = Blueprint("event_route", __name__)

# Cria uma rota "event" com o método POST
@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
    return jsonify({"estou": "aqui"}), 201