from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators, PasswordField
from .models import db, User

class ContactForm(Form):
	name = StringField('Name', [validators.Required('Please enter your name')])
	email = StringField('Email', [validators.Required('Please enter your email id'), validators.Email('Please enter a valid id')])
	subject = StringField('Subjet', [validators.Required('Please enter a subject for the message')])
	message = TextAreaField('Message', [validators.Required('Please enter the message')])


class SignupForm(Form):
	username = StringField("username",  [validators.Required("Please enter your username")])
	name = StringField("Name",  [validators.Required("Please enter your name.")])
	email = StringField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	password = PasswordField('Password', [validators.Required("Please enter a password.")])

	def __init__(self, *args, **kwargs):  
		Form.__init__(self, *args, **kwargs)

	def validate(self):  
		if not Form.validate(self):
			return False

		user = User.query.filter_by(email = self.email.data).first()
		if user:   
			self.email.errors.append("That email is already taken")
			return False
		else:
			user = User.query.filter_by(username = self.username.data).first()
			if user:
				self.email.errors.append("That username is already taken")
				return False
			return True


class SignInForm(Form):
	username = StringField("username",  [validators.Required("Please enter your username")])	
	password = PasswordField('password', [validators.Required("Please enter your password.")])

	def __init__(self, *args, **kwargs):  
		Form.__init__(self, *args, **kwargs)

	def validate(self):  
		if not Form.validate(self):
			return False

		user = User.query.filter_by(username = self.username.data).first()
		if user and user.check_password(self.password.data):   			
			return True
		else:
			self.username.errors.append("Invalid username or password")
			return False
			