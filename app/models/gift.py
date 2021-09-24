# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')  # 引用user模型
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)  # user.id中user为line 9
    book = relationship('Book')  # 引用book模型
    bid = Column(Integer, ForeignKey('book.id'), nullable=False)  # book.id中user为line 11
