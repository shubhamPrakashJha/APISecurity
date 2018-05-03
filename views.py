from database_setup import Base, User
from flask import Flask, jsonify, request, url_for, abort
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from flask import Flask

engine = create_engine('sqlite:///users.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

@app.route('/users', methods=['POST'])
def new_user():
	# return "create New User"
	username = request.json.get('username')
	password = request.json.get('password')

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
