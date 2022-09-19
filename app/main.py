from app import wsgi_app
from flask import render_template, redirect
from .data import db_handler, event_data
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


@wsgi_app.route('/events/list')
def events():
    events_list = db_handler.get_all_events()
    return render_template('events.html', events=events_list)


@wsgi_app.route('/events/add')
def add_event():
    db_handler.add_event(event_data(1, None, 'ABC', 'HAIFGDSAHGNBP'))
    return redirect('/events/list')