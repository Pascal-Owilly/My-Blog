from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fekvoeogziqrlf:d9594531e7c3f82a9967301bb0716a556147356c23ee55c598dfa5c4caaae775@ec2-54-85-113-73.compute-1.amazonaws.com:5432/d7h5rjmt8nffud'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from blog import routes