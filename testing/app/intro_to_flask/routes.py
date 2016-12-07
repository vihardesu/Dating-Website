from intro_to_flask import app
from flask import render_template, request, flash, session, redirect, url_for
from forms import ContactForm, SignupForm, SigninForm, BlogForm, DateForm
from flask_mail import Message, Mail
from models import db, User, Post, Date
 
mail = Mail()

#Links to the Home Page 
@app.route('/')
def home():
  posts = Post.query.all()
  return render_template('home.html', posts=posts)
  #return render_template('show_entries.html', post=post)

@app.route('/dateview')
def dateview():
  dates = Date.query.all()
  return render_template('dateview.html', dates=dates)

#Links to the About Page 
@app.route('/about')
def about():
  return render_template('about.html')

#Links to Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='contact@example.com', recipients=['vihardesu@gmail.com'])
      msg.body = """
      From: %s @ Email: %s
      Message:
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
 
      return render_template('contact.html', success=True)
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

#Links to Signup Form
@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()

  if 'email' in session:
    return redirect(url_for('profile'))
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:   
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()
      session['email'] = newuser.email
      return redirect(url_for('profile'))
   
  elif request.method == 'GET':
    return render_template('signup.html', form=form)

@app.route('/profile')
def profile():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
 
  user = User.query.filter_by(email = session['email']).first()
 
  if user is None:
    return redirect(url_for('signin'))
  else:
    return render_template('profile.html')

#Signin Route
@app.route('/signin', methods=['GET', 'POST'])
def signin():
  form = SigninForm()

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

#Signout Route
@app.route('/signout')
def signout():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
     
  session.pop('email', None)
  return redirect(url_for('home'))

#Date Route
@app.route('/date', methods=['GET', 'POST'])
def date():
  form = DateForm()

  if request.method == 'POST':
    if form.validate() == False:
      return render_template('date.html', form=form)
    else:
      newdate = Date(request.form['firstname'], request.form['lastname'], request.form['email'], request.form['hobbies'])
      #newpost = Post(form.title.data, form.post.data)
      db.session.add(newdate)
      db.session.commit()
      return redirect(url_for('dateview'))


  elif request.method == 'GET':
    return render_template('date.html', form=form)


#Blog Route
@app.route('/blog', methods=['GET', 'POST'])
def blog():
  form = BlogForm()

  if request.method == 'POST':
    if form.validate() == False:
      return render_template('blog.html', form=form)
    else:
      newpost = Post(request.form['title'], request.form['post'])
      #newpost = Post(form.title.data, form.post.data)
      db.session.add(newpost)
      db.session.commit()
      return redirect(url_for('home'))


  elif request.method == 'GET':
    return render_template('blog.html', form=form)

if __name__ == '__main__':
  app.run(debug=True)
