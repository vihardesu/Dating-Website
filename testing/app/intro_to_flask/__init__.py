from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Message, Mail
 
mail = Mail()
 
app = Flask(__name__)

#This line handles CSRF Attacks 
app.secret_key = 'ad098a0f098f2098'

#Mail Rendering
#This allows for Gmail servers specifically
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'vihardesu@gmail.com'
app.config["MAIL_PASSWORD"] = 'Dieasche1'
 
mail.init_app(app) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:chocolate@localhost/development'
 
from models import db
db.init_app(app)

import intro_to_flask.routes
