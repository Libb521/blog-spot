from flask import render_template
from app import app
# from ..models import User, Blogpost

#views
@app.route('/')
def index():

    # posts = Blogpost.query.all()
    title = 'Blog spot'
    message = 'Welcome to Libby blogs'
    return render_template('index.html', message = message, title = title)

@app.route('/blog')
# @login_required
def blog():

    # posts = Blogpost.query.all()
    title = 'Blog spot'
    return render_template('blog.html', title = title)