from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, SmallInteger, Integer, NVARCHAR, String, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


def explict_repr(self):
    d = {}
    for v in dir(self.__class__):
        if not v.startswith('_'):
            d.update({v: getattr(self, v)})
    return str(d)


Base = declarative_base()
setattr(Base, '__repr__', explict_repr)


# class Book(Base):
#     """
#     自定义模型类
#     """
#     __tablename__ = 'book'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     isbn = Column(String(15), nullable=False, unique=True)
#     title = Column(String(50), nullable=False)
#     author = Column(String(30), default='未名')
#     binding = Column(String(20))
#     image = Column(String(50))
#     pages = Column(Integer)
#     price = Column(String(20))
#     pubdate = Column(String(20))
#     publisher = Column(String(50))
#     summary = Column(String(1000))
#
#
# class Gift(Base):
#     __tablename__ = 'gift'
#
#     id = Column(Integer, primary_key=True)
#     # user = db.relationship('User')
#     uid = Column(Integer, ForeignKey('user.id'))
#     isbn = Column(String(13), nullable=False)
#     launched = Column(Boolean, default=False)
#
#
# class User(Base):
#     __tablename__ = 'user'
#
#     id = Column(Integer, primary_key=True)
#     nickname = Column(String(24), nullable=False)
#     _password = Column('password', String(128), nullable=False)  # 在Column的第一个字符串字段作数据库的字段
#     phone_number = Column(String(18), unique=True)
#     email = Column(String(50), unique=True, nullable=False)
#     confirmed = Column(Boolean, default=True)
#     beans = Column(Float, default=0)
#     send_counter = Column(Integer, default=0)
#     receive_counter = Column(Integer, default=0)
#     wx_open_id = Column(String(50))
#     wx_name = Column(String(32))
from werkzeug.security import generate_password_hash, check_password_hash
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    _password = Column('password', String(128))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        self._password = generate_password_hash(pwd)


connection_repr = 'mysql+pymysql://root:noki@123@10.57.150.116:3306/new_fisher'
engine = create_engine(connection_repr)
DbSession = sessionmaker(bind=engine)
session = DbSession()
print(1)
