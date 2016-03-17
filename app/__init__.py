from flask import Flask

app = Flask(__name__)
pp = Flask(__name__)   
app.secret_key = 'development key'   
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = 'sarthaks93@gmail.com'
app.config["MAIL_PASSWORD"] = '########'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rhcpsnow@localhost/flaskdb'
 
from .models import db
db.init_app(app)

from app import views