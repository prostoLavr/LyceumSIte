from app import wsgi_app
from flask import render_template
import datetime


@wsgi_app.route('/')
def index():
    return render_template('index.html')


@wsgi_app.route('/timetable')
def timetable():
    state = datetime.datetime.today().weekday()
    return render_template('timetable.html', state=state)


@wsgi_app.route('/lessons')
def lessons():
    state = datetime.datetime.today().weekday()
    return render_template('lessons.html', state=state)