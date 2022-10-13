from flask import Flask,  redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import hashlib

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(seconds=10)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/flask_tester_1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100))

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

@app.route('/')
def home():
    users = Users.query.all()
    return render_template('base.html', user_lst=users)

@app.route('/user', methods=['POST', 'GET'])
def user():
    if 'user' in session:
        user_name = session['user']
        if request.method == 'POST':
            email = request.form['user-email']
            session['email'] = email
            user_in_db = Users.query.filter_by(name=user_name).first()
            user_in_db.email = email
            db.commit()
            flash('Email was saved')
        else:
            if email in session:
                email = session['email']
            else:
                email = ''
        return render_template('user.html', name=user_name, email=email)
    else:
        flash('You are not logged in')
        return redirect(url_for('login'))



@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        session.permanent = True
        user_name = request.form['user-name']
        user_pass = hashlib.md5(request.form['user-pass'].encode()).hexdigest()
        user_in_db = Users.query.filter_by(name=user_name).first()
        if user_in_db:
            if user_pass == user_in_db.password:
                session['user'] = user_name
                session['email'] = user_in_db.email
                return redirect(url_for('user', name=user_name, email=user_in_db.email))
            else:
                flash('Wrong password')
                return redirect(url_for('login'))
        else:
            new_user = Users(user_name, user_pass, '')
            db.session.add(new_user)
            db.session.commit()
            session['name'] = user_name
            session['email'] = ''
            flash('User was created')
            return redirect(url_for('user', name=user_name))
    else:
        if 'user' in session:
            return redirect(url_for('user', name=session['user']))
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('email', None)
    flash('You were Logged out')
    return redirect(url_for('user', name="Admin"))





@app.route('/admin')
def admin():
    return redirect()


if __name__  == '__main__':

    app.run(debug=True)