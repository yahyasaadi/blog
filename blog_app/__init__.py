from flask import Flask, render_template

app = Flask(__name__)

from blog_app import routes