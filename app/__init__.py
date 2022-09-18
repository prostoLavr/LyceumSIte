from flask import Flask

wsgi_app = Flask(__name__)

from . import main
