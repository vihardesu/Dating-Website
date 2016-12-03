from intro_to_flask import app
from flask import render_template, request, flash, session, url_for, redirect
from forms import SignUp, SignIn
from models import db, User

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignUp()

  if 'email' in session:
  return redirect(url_for('profile'))
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:   
      newuser = User(form.username.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()
        
          session['email'] = newuser.email
          
     return redirect(url_for('polling'))
   
  elif request.method == 'GET':
    return render_template('signup.html', form=form)
    
@app.route('/signin', methods=['GET', 'POST'])
def signin():
  form = Signin()

  if 'email' in session:
  return redirect(url_for('profile'))
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signin.html', form=form)
    else:
      session['email'] = form.email.data
      return redirect(url_for('profile'))
                 
  elif request.method == 'GET':
    return render_template('signin.html', form=form)
    
@app.route('/polling')
def polling():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
 
  user = User.query.filter_by(email = session['email']).first()
 
  if user is None:
    return redirect(url_for('signin'))
  else:
    return render_template('polling.html')

@app.route('/signout')
def signout():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
     
  session.pop('email', None)
  return redirect(url_for('home'))

 if __name__ == '__main__':
  app.run(debug=True)
