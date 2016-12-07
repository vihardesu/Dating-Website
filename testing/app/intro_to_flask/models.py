from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
 
db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))
   
  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)
  
  #Salted Hash Password
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)
   
  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)

class Post(db.Model):
  __tablename__ = 'posts'
  uid = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(100))
  post = db.Column(db.String(500))

  def __init__(self, title, post):
    self.title = title.title()
    self.post = post.title()

class Date(db.Model):
  __tablename__ = 'dates'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  hobbies = db.Column(db.String(500))


  def __init__(self, firstname, lastname, email, hobbies):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.title()
    self.hobbies = hobbies.title()






