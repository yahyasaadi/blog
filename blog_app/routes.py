from flask import render_template
from blog_app import app

# routes
@app.route('/')
def home():
    title="Home"
    return render_template('home.html', title=title)