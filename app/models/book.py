import json
from sqlalchemy import Column, Integer, String
from .base import Base, db


class Book(Base):
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

    @classmethod
    def write_book(cls, d: dict):
        book = cls(isbn=d.get('isbn'),
                   title=d.get('title'),
                   author=d.get('author', ''),
                   binding=d.get('binding', ''),
                   image=d.get('image', ''),
                   page=d.get('page', ''),
                   price=d.get('price', ''),
                   pubdate=d.get('pubdate', ''),
                   publisher=d.get('publisher', ''),
                   summary=d.get('summary', ''))
        db.session.add(book)
        db.session.commit()


if __name__ == '__main__':
    print(1)
