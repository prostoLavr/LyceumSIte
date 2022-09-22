from app import wsgi_app, config
from flask import render_template, redirect
from .data import db_handler, event_data, timetable_data, short_timetable_data
import datetime


@wsgi_app.route('/')
def index():
    return render_template('index.html')


@wsgi_app.route('/timetable')
def timetable():
    state = datetime.datetime.now()
    if datetime.time(state.hour, state.minute) > config.last_lesson_time:
        state = {2: 1, 3: 1, 4: 1, 5: 2, 6: 0}.get(state.weekday() + 1, state.weekday() + 1)
    else:
        state = {2: 1, 3: 1, 4: 1, 5: 2, 6: 0}.get(state.weekday(), state.weekday())
    return render_template('timetable.html', timetable_data=timetable_data[str(state)], state=state)


@wsgi_app.route('/lessons')
def lessons():
    state = datetime.datetime.now()
    if datetime.time(state.hour, state.minute) > config.last_lesson_time:
        state = state.weekday() + 1
    else:
        state = state.weekday()
    data = db_handler.get_lessons(state, '10b')
    data.pop('day')
    return render_template('lessons.html', state=state, lessons_data=data.items(),
                           timetable_data=short_timetable_data[str({2: 1, 3: 1, 4: 1, 5: 2, 6: 0}.get(state, state))])


@wsgi_app.route('/events/list')
def events():
    events_list = db_handler.get_all_events()
    return render_template('events.html', events=events_list)


@wsgi_app.route('/events/add')
def add_event():
    db_handler.add_event(event_data(1, None, 'ABC', 'HAIFGDSAHGNBP'))
    return redirect('/events/list')


@wsgi_app.route('/events/event/<int:id>')
def event(id):
    e = db_handler.get_event(id)
    return render_template('event.html', event=e)
