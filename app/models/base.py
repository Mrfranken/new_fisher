from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    # create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def set_value_for_table(self, value_dict: dict):
        for k, v in value_dict.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)
