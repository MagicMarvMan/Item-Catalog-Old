from flask import Flask, Reponse

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return "Hello World!"