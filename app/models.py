from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
 
db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(100))
  name = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  password = db.Column(db.String(54))
   
  def __init__(self, username, name, email, password):
    self.username = username
    self.lastname = lastname
    self.email = email
    self.set_password(password)
     
  def set_password(self, password):
    self.password = generate_password_hash(password)
   
  def check_password(self, password):
    return check_password_hash(self.password, password)