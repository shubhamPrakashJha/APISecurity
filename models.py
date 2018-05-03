from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context

Base = declarative_base()

engine = create_engine('sqlite:///users.db')

Base.metadata.create_all(engine)
