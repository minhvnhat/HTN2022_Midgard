# Import the Flask library + some others we will use later
from flask import Flask, jsonify, request, session
from datetime import timedelta
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# Create a Flask object.
app = Flask(__name__)
app.permanent_session_lifetime = timedelta(days=5)
app.secret_key='hello'

db = SQLAlchemy(app)
class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    psw = db.Column(db.String(30))

    def __init__(self, username, psw):
        self.username = username
        self.psw = psw

# Create our first route which returns the string "hello". 
@app.route('/', methods=['GET'])
def index():
  return "hello"

@app.route('/login', methods=['POST'])
def login():
    session.permanent = True
    user = request.form['username']
    session['user'] = user

    found_user = User.query.filter_by(name=user).first()
    if found_user:
        return "email used"
    else:
        usr = User(user, "")
        db.session.add(usr)
        db.session.commit()

    return f"user"

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    psw = request.form(['psw'])
    return 'register success'

@app.route('/profile', methods=['GET'])
def profile():
    if 'user' in session:
        user = session['user']
        # send user profile
        return f'profile success, user {user}'
    else:
        return 'profile not logged in'

@app.route('/logout')
def logout():
    session.pop("user", None) 

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True) 