from flask import Flask, render_template


wsgi_app = Flask(__name__)


@wsgi_app.route('/')
def index():
    return render_template('index.html')

