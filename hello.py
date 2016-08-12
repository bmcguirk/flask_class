import os
from flask import Flask, request, render_template, url_for, redirect, flash
app = Flask(__name__)

@app.route('/')
def index():
    return url_for('show_user_profile',username='brian')

@app.route('/login', methods=["GET","POST"])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],request.form['password']):
            flash("Successfully logged in.")
            # return "Welcome back, {}".format(request.form["username"])
            return redirect(url_for('welcome',username=request.form.get('username')))
        else:
            error = "Incorrect username and password."
    return render_template('login.html', error=error)
        
def valid_login(username,password):
    if username == password:
        return True
    else:
        return False
        
@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html')


if __name__ == '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT',5000))
    app.debug = True
    app.secret_key = 'SuperSecret'
    app.run(host=host,port=port)
    