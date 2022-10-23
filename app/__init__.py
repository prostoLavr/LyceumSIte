from flask import Flask
from . import data

wsgi_app = Flask(__name__)
data.global_init()

from . import main
