from flask import redirect, render_template, url_for
from blog_app import app
from blog_app.forms import RegistrationForm, LoginForm, PostForm

# routes
@app.route('/')
def home():
    title="Home"
    return render_template('home.html', title=title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('register.html', form=form, title='Register Form')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html', form=form, title='Login Form')


@app.route('/post/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('new_post.html', form=form, title='New Post')