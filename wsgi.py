from flask import Flask


wsgi_app = Flask(__name__)


@wsgi_app.route('/')
def index():
    return '<h1>Вас приветствует сайт Лицея №2</h1>'

