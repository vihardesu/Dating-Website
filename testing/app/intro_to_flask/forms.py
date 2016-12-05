#from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError


 
class ContactForm(FlaskForm):
  name = TextField("Name", validators=[DataRequired("Please Enter Name.")])
  email = TextField("Email", validators=[DataRequired("Please Enter Email.")])
  subject = TextField("Subject", validators=[DataRequired("Please Enter Subject.")])
  message = TextAreaField("Message", validators=[DataRequired("Please Enter Message.")])
  submit = SubmitField("Send")