from turtle import title
from flask import Flask,render_template

# creating application instance
app = Flask(__name__)

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
        'title':'Her journer to somewhere',
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

    title = 'About'
    return render_template('about.html', title = title)    
 

if __name__=='__main__':
    app.run(debug=True)     






