from flask import Flask
## arquivo de configuração do servidor
from config import app_config


def create_app(config_name):
  config = app_config[config_name]
  app = Flask(__name__, template_folder="templates")

  app.secret_key = config.SECRET
  app.config.from_object(app_config[config_name])
  app.config.from_pyfile("config.py")

  @app.route("/")
  def index():
    return "Flask api testes"

  return app