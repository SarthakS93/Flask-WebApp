from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators

class ContactForm(Form):
	name = StringField('Name', [validators.Required('Please enter your name')])
	email = StringField('Email', [validators.Required('Please enter your email id'), validators.Email('Please enter a valid id')])
	subject = StringField('Subjet', [validators.Required('Please enter a subject for the message')])
	message = TextAreaField('Message', [validators.Required('Please enter the message')])