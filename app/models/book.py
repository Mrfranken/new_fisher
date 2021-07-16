import json
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    isbn = Column(String(15), nullable=False, unique=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    image = Column(String(100))
    page = Column(Integer)
    price = Column(String(20))
    pubdate = Column(String(20))
    publisher = Column(String(50))
    summary = Column(String(1000))
