from flask import Flask
from src.main.routes.event import event_route_bp # importa o agregador de rotas

app = Flask(__name__) # cria um server http

app.register_blueprint(event_route_bp) # registra o blueprint no apps