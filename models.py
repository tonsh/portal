#coding=utf-8
''' Tables mapper '''

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from database import Database

Base = declarative_base()

def create_db():
    engine = Database.instance().get_engine()
    Base.metadata.create_all(engine)

class Category(Base):
    ''' category table '''
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    parent = Column(Integer, nullable=False, default=0)
    create_at = Column(DateTime, nullable=False) 

    images = relationship('Image',
                order_by="Image.id",
                backref='category')

    def __repr__(self):
        return "<Category('%s')>" % (self.title)


class Image(Base):
    ''' image table '''
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=True)
    content = Column(Text, nullable=True)
    cid = Column(Integer, ForeignKey('categories.id'), nullable=False)
    create_at = Column(DateTime, nullable=False)

    category = relationship("Category",
                            backref=backref('images', order_by=id))

    def __repr__(self):
        return "<Image('%s')>" % (self.title)
