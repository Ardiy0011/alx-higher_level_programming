#!/usr/bin/python3
"""
class to connect to databasd and name
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
Base = declarative_base()


class City(Base):
    """derive class of base declarative"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
