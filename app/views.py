from app import app
from flask import Flask, render_template, request, flash
from .forms import ContactForm
from flask.ext.mail import Message, Mail
from .models import db

mail = Mail(app)

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/about')  
def about():
	return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()

	if request.method == 'POST':
		if not form.validate():
			flash('All fields required')
			return render_template('contact.html', form = form)
		else:
			msg = Message(form.subject.data, sender = app.config['MAIL_USERNAME'], recipients=[form.email.data,])
			msg.body = form.message.data
			mail.send(msg)
			return render_template('contact.html', success = True)
	elif request.method == 'GET':
		return render_template('contact.html', form = form)

@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'
