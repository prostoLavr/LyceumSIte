import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec
from collections import namedtuple
import os


db_path = os.path.join('app', 'data', 'data.db')

SqlAlchemyBase = dec.declarative_base()
event_data = namedtuple('event_data', ['id', 'date', 'name', 'desc'])

__factory = None


def global_init():
    global __factory, db_path

    if __factory:
        return

    db_path = db_path.strip()
    if not db_path:
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = f'sqlite:///{db_path}?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from .event import Event

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()