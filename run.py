import sys
import os
from app import create_app
from config import app_config, app_active

environment = os.environ['FLASK_ENV'] = "development"
config = app_config[environment]
config.APP = create_app(environment)

if __name__ == '__main__':
  config.APP.run(host=config.IP_HOST, port=config.PORT_HOST)
  # reload(sys)