from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    isbn = Column(String(15), nullable=False, unique=True)
    author = Column(String(30), default='未名')
    title = Column(String(30), nullable=False)
    price = Column(String(20))
    binding = Column(String(20))
