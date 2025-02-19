from flask import Flask

# Importando os agregadores de rota
from src.main.routes.event import event_route_bp
from src.main.routes.subs import subs_route_bp

# Cria um server http
app = Flask(__name__)

# Registra o bp no server
app.register_blueprint(event_route_bp)
app.register_blueprint(subs_route_bp)