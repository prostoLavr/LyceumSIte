from flask import Flask
from flask_bootstrap import Bootstrap

wsgi_app = Flask(__name__)
bootstrap = Bootstrap(wsgi_app)

from . import main
