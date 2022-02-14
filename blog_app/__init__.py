from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ghnkjilo765fhy87hbgtr45'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://yahya:Noor_main_db@localhost/blog'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from blog_app import routes