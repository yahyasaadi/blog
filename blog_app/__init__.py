from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ghnkjilo765fhy87hbgtr45'



from blog_app import routes