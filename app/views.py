from app import app
from flask import Flask, render_template, request, flash, session, url_for, redirect
from .forms import ContactForm, SignupForm, SignInForm
from flask.ext.mail import Message, Mail
from .models import db, User

mail = Mail(app)

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/about')  
def about():
	return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	
	if request.method == 'POST':
		form = ContactForm(request.form)
		if not form.validate():
			return render_template('contact.html', form = form)
		else:
			msg = Message(form.subject.data, sender = app.config['MAIL_USERNAME'], recipients=['sarthakfloyd@gmail.com',])
			msg.body = form.message.data
			mail.send(msg)
			return render_template('contact.html', success = True)
	elif request.method == 'GET':
		form = ContactForm()
		return render_template('contact.html', form = form)


@app.route('/testdb')
def testdb():
	if db.session.query("1").from_statement("SELECT 1").all():
		return 'It works.'
	else:
		return 'Something is broken'


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if 'username' in session:
		return redirect(url_for('profile'))  
	
	if request.method == 'POST':
		form = SignupForm(request.form)
		if not form.validate():
			return render_template('signup.html', form = form)
		else:
			newuser = User(form.username.data, form.name.data, form.email.data, form.password.data)
			db.session.add(newuser)
			db.session.commit()
			session['username'] = newuser.username
			return redirect(url_for('profile'))
	elif request.method == 'GET':
		form = SignupForm()
		return render_template('signup.html', form = form)

@app.route('/profile')
def profile():
	if 'username' not in session:
		return redirect(url_for('signin'))
	user = User.query.filter_by(email = session['email']).first()
	if user is None:
		return redirect(url_for('signin'))
	else:
		return render_template('profile.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
	if 'username' in session:
		return redirect(url_for('profile'))
	
	if request.method == 'POST':
		form = SignInForm(request.form)
		if not form.validate():
			return render_template('signin.html', form = form)
		else:
			session['username'] = form.username.data
			return redirect(url_for('profile'))
	elif request.method == 'GET':
		form = SignInForm()
		return render_template('signin.html', form = form)


@app.route('/signout')
def signout():
 
  if 'username' not in session:
    return redirect(url_for('signin'))
     
  session.pop('username', None)
  return redirect(url_for('home'))
  
