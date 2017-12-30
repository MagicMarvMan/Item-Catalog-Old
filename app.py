from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("home.html",title="Home")

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)

if(__name__ == '__main__'):
	app.run(host="0.0.0.0")