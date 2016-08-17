import os
from flask import Flask, request, render_template, url_for, redirect, flash, session
app = Flask(__name__)

# @app.route('/')
# def index():
#     return url_for('show_user_profile',username='brian')

@app.route('/login', methods=["GET","POST"])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],request.form['password']):
            flash("Successfully logged in.")
            # return "Welcome back, {}".format(request.form["username"])
            # return redirect(url_for('welcome',username=request.form.get('username')))
            # response = make_response(redirect(url_for('welcome',username=request.form.get('username'))))
            # response.set_cookie('username', request.form.get('username'))
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = "Incorrect username and password."
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    # response = make_response(redirect(url_for('login')))
    # response.set_cookie('username','', expires=0)
    # return response
    session.pop('username', None)
    return redirect(url_for('login'))

def valid_login(username,password):
    if username == password:
        return True
    else:
        return False
        
@app.route('/')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT',5000))
    app.debug = True
    app.secret_key = '\x1c\xf4U\xf5aD\xf6\x80\xf0\xa6\x7f\xed[\xd9\x81yIU\xc3\xe7\x83]\xe8\xae'
    app.run(host=host,port=port)
    