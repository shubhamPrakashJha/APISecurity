from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context

Base = declarative_base()


class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	username = Column(String(32), index=True)
	password_hash = Column(String(64))

	def hash_password(self, password):
		print "create hash value of the password and store in database"

	def verify_password(self, password):
		print "verify the hash value of given password with stored hash value"


engine = create_engine('sqlite:///users.db')

Base.metadata.create_all(engine)
