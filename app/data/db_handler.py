from . import create_session, event_data, lessons_data
from .event import Event
import datetime


def add_event(data: event_data):
    """Add event to db

    :param data: data.date=None for auto
    :return:
    """
    if data.date is None:
        data = event_data(id=data.id, date=datetime.datetime.now(), name=data.name, desc=data.desc)
    event = Event(id=data.id, date=data.date, name=data.name, desc=data.desc)
    db_sess = create_session()
    db_sess.add(event)
    db_sess.commit()


def get_all_events():
    db_sess = create_session()
    events = db_sess.query(Event).all()
    return events


def get_event(event_id):
    db_sess = create_session()
    e = db_sess.query(Event).filter_by(id=event_id).first()
    return e


def get_lessons(weekday: int, cls: str) -> dict:
    """

    :param weekday: 0~6
    :param cls: {8-11}{a,b,v}
    :return:
    """
    weekday %= 6
    return [i.copy() for i in lessons_data[cls] if i['day'] == weekday][0]
