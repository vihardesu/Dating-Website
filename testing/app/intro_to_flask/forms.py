from flask_wtf import Form
from wtforms import StringField, TextField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import Required, ValidationError, Email
from models import db, User, Post, Date


#Contact Form 
class ContactForm(Form):
  name = TextField("Name", validators=[Required("Please Enter Name.")])
  email = TextField("Email", validators=[Required("Please Enter Email."), Email("Please enter a valid email address.")])
  subject = TextField("Subject", validators=[Required("Please Enter Subject.")])
  message = TextAreaField("Message", validators=[Required("Please Enter Message.")])
  submit = SubmitField("Send")

#Sign-up Form
class SignupForm(Form):
  firstname = TextField("First name",  validators=[Required("Please Enter First Name.")])
  lastname = TextField("Last name", validators=[Required("Please Enter Last Name.")])
  #Add email verification from flask-wtf
  email = TextField("Email",  [Required("Please enter your email address."), Email("This field requires a valid email address")])
  password = PasswordField('Password', validators=[Required("Please Enter a Password.")])
  submit = SubmitField("Create account")
 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user:
      self.email.errors.append("That email is already taken")
      return False
    else:
      return True
#Signin Form
class SigninForm(Form):
  email = TextField("Email",  [Required("Please enter your email address."), Email("This field requires a valid email address")])
  password = PasswordField('Password', validators=[Required("Please Enter a Password.")])
  submit = SubmitField("Sign In")
   
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user and user.check_password(self.password.data):
      return True
    else:
      self.email.errors.append("Invalid e-mail or password")
      return False

#BlogPost Form
class BlogForm(Form):
  title = TextField("Title", validators=[Required("Please Enter Title.")])
  post = TextAreaField("Post", validators=[Required("Please Enter Content for your Post.")])
  submit = SubmitField("Post!")

  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)

#Update Form
class BlogForm(Form):
  title = TextField("Title", validators=[Required("Please Enter Title.")])
  post = TextAreaField("Post", validators=[Required("Please Enter Content for your Post.")])
  submit = SubmitField("Post!")

  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)

#Update Form
class DateForm(Form):
  firstname = TextField("First name",  validators=[Required("Please Enter First Name.")])
  lastname = TextField("Last name", validators=[Required("Please Enter Last Name.")])
  #Add email verification from flask-wtf
  email = TextField("Email",  [Required("Please enter your email address."), Email("This field requires a valid email address")])
  hobbies = TextAreaField("Hobbies", validators=[Required("Please Enter Your Hobbies.")])
  submit = SubmitField("Post!")

  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
























