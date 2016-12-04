from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from models import db, User

#presence validator to ensure field is filled in 
class SignUp(Form):
  username = TextField("Username",  [validators.Required("Enter a username.")])
  email = TextField("Email", [validators.Required("Enter your email address."), validators.Email("Enter your email address.")])
  password = PasswordField('Password', [validators.Required("Enter a password.")])
  submit = SubmitField("Create account")
 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user:
      self.email.errors.append("Email is already in use")
      return False
    else:
      return True
      
class Signin(Form):
  email = TextField("Email",  [validators.Required("Enter your email address."), validators.Email("Enter your email address.")])
  password = PasswordField('Password', [validators.Required("Enter your password.")])
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
      self.email.errors.append("Incorrect email address or password")
      return False