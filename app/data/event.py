import sqlalchemy as sa
from . import SqlAlchemyBase


class Event(SqlAlchemyBase):
    __tablename__ = 'events'
    id = sa.Column(sa.Integer, sa.Sequence('seq_reg_id', start=1, increment=1), primary_key=True)
    date = sa.Column(sa.DateTime)
    name = sa.Column(sa.String, nullable=False)
    desc = sa.Column(sa.Text, default='')

    def __repr__(self):
        return f'<File {self.id} {self.name}>'