
from flask import Flask,render_template, url_for
from forms import RegistrationForm, LoginForm

# creating application instance
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd89bd8891e344e4b50facbe3f9ec092b'

# dummy database call
posts = [
    {
        'title':'My journey to the wild',
        'author':'Pascal Owilly',
        'comment':'It was fun',
        'date_posted':'June 11 2022'
    },
    {
        'author':'Jane Kameme',
        'title':'Her journer to the past',
        'comment':'It was cool',
        'date_posted':'June 20 2022'
    },
]

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', posts = posts)

@app.route('/about')
def about():

  
    return render_template('about.html', title = 'About')    


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register',form=form)    

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'login',form=form)    

if __name__=='__main__':
    app.run(debug=True)     






