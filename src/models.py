import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Basic_Characters(Base):
    __tablename__ = 'Basic_Characters'
    uid = Column(Integer, primary_key=True)
    name = Column(String(200))

class Properties_Characters(Base):
    __tablename__ = 'Properties_Characters'
    id = Column(Integer, primary_key=True) 
    uid = Column(Integer, ForeignKey('Basic_Characters.uid'))
    height = Column(Float)
    mass = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(String(50))
    gender = Column(String(50))
    created = Column(DateTime)
    edited = Column(DateTime)
    homeworld = Column(Integer, ForeignKey('Basic_Characters.uid'))
    description = Column(String(250))
    url = Column(String(250))

class Basic_Planets(Base):
    __tablename__ = 'Basic_Planets'
    uid = Column(Integer, primary_key=True)
    name = Column(String(200))

class Properties_Planets(Base):
    __tablename__ = 'Properties_Planets'
    id = Column(Integer, primary_key=True) 
    uid = Column(Integer, ForeignKey('Basic_Planets.uid'))
    diameter = Column(Float)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(Float)
    population = Column(Integer)
    climate = Column(String(50))
    terrain = Column(String(50))
    surface_water = Column(Integer)
    created = Column(DateTime)
    edited = Column(DateTime)
    url = Column(String(250))  

class User_Profile(Base):
    __tablename__ = 'User_Profile'
    uid = Column(Integer, primary_key=True)
    name = Column(String(200)) 

class Detail_Profile(Base):
    __tablename__ = 'Detail_Profile'
    id = Column(Integer, primary_key=True) 
    uid = Column(Integer, ForeignKey('User_Profile.uid'))
    age = Column(Integer)
    nation = Column(String(80))

class User_Favorites(Base):
    __tablename__ = 'User_Favorites'
    id = Column(Integer, primary_key=True) 
    uid_User = Column(Integer, ForeignKey('User_Profile.uid'))
    uid_Character = Column(Integer, ForeignKey('Basic_Characters.uid'))
    uid_Planets = Column(Integer, ForeignKey('Basic_Planets.uid'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')