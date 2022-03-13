from flask import Flask,render_template

# creating application instance
app = Flask(__name__)

# dummy database call
posts = [
    {
        'author':'Pascal Owilly',
        'title':'My journey to the wild',
        'comment':'It was fun',
        'date_posted':'June 11 2022'
    },
    {
        'author':'Pascal Owilly',
        'title':'My journey to the wild',
        'comment':'It was fun',
        'date_posted':'June 11 2022'
    },
]

@app.route('/')
def index():

    first_name = "Pascal"
    favourite_food = "Pilau with Chapati"
    bucketlist = ["Visit Salar de Uyuni","Visit glass bridge to shake a little","Visit bioluminiscence near caribean sea in Jamaica", 75]
    
    return render_template('index.html',
     first_name=first_name,
     favourite_food=favourite_food,
      bucketlist= bucketlist,
      posts=posts)

@app.route('/signin/<name>')
def signin():
    return render_template('signin.html')    

# Invalid URL
app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal server error
app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500  

if __name__=='__main__':
    app.run(debug=True)     






