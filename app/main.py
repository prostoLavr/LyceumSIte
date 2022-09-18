from app import wsgi_app
from flask import render_template


@wsgi_app.route('/')
def index():
    return render_template('index.html')


@wsgi_app.route('/timetable')
def timetable():
    return render_template('timetable.html')