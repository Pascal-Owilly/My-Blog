from flask import Flask, render_template, url_for, flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post


posts = [
    {
        'author': 'Barak Obama',
        'title': 'Economy',
        'content': 'We fight to remove the daily chronicles of economic inconsistency',
        'date_posted': 'May 1, 2022'
    },
    {
        'author': 'Cool James',
        'title': 'Blockchain',
        'content': 'Early in 2000s no on knew how hard the .com era will hit the world be cause they were in the middle of it',
        'date_posted': 'May 7, 2022'
    }
]


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)