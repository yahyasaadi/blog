from flask import redirect, render_template, url_for, flash
from blog_app import app, db, bcrypt, login_manager
from blog_app.forms import RegistrationForm, LoginForm, PostForm
from blog_app.models import User, Post, Comment
from flask_login import current_user, login_user, logout_user, login_required


# routes
@app.route('/')
def home():
    title="Home"
    return render_template('home.html', title=title)


# The registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register Form')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Log in unsuccessful. Please check email and password!', 'danger')
    return render_template('login.html', form=form, title='Login Form')



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route('/post/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('new_post.html', form=form, title='New Post')