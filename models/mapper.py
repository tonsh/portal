#coding=utf-8
''' Tables mapper '''

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from models.database import Base
from models.database import Database

Database.instance().create_db()
