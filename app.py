import os
import os.path
if(os.path.isfile("restaurantmenu.db")):
	os.remove("restaurantmenu.db")
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem, create_db
from flask import session as login_session
import random
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
import string

app = Flask(__name__)
app.secret_key = "aeiruh3gaoj56h9zb8m3v903p9g48avz96hga3j8qck9p9878rs87V=%(/BAG{GGAB/&B=N/ZSG"

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

create_db()

@app.route("/")
@app.route("/index")
def index():
	return render_template("home.html",title="Home")

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)

if(__name__ == '__main__'):
	app.run(host="0.0.0.0")