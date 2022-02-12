from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ghnkjilo765fhy87hbgtr45'
app.config['SQLALCHEMY_DATABASE_URI'] = ''

db = SQLAlchemy(app)

from blog_app import routes