from flask import render_template
from app import app

#views
@app.route('/')
def index():

    
    title = 'Blog spot'
    message = 'Welcome to Libby blogs'
    return render_template('index.html', message = message, title = title)

# @app.route('/user/<uname>')
# # @login_required
# def profile(uname):
#     user = User.query.filter_by(username = uname).first()

#     if user is None:
#         abort(404)

#     return render_template("profile/profile.html", user = user)

# # @app.route('/blog/')
# # @login_required
# def blog():
#     '''
#     View root page function that returns the index page and its data
#     '''
    
#     # posts = Blogpost.query.all()
#     title = 'Blog spot'  
#     return render_template('blog.html', title = title)

# @app.route('/add/')
# def add():
    
#     title = 'Blog spot'  
#     return render_template('add.html', title = title )

# @app.route('/addpost/', methods=['POST'])
# def addpost():
    
#     title = request.form['Title']
#     subtitle = request.form['Subtitle']
#     author = request.form['Author']
#     content = request.form['Content']
   

#     post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

#     db.session.add(post)
#     db.session.commit()

#     return  redirect(url_for('main.blogpage'))

# @app.route('/post/')
# def post():

    
#     return render_template('post.html' )


# @app.route('/about/')
# # @login_required
# def about():
    
#     title = 'BLOGG SITE'  
#     return render_template('about.html', title = title )




# @app.route('/blog/<int:id>')
# # @login_required
# def get_blog(id):

#     blog = get_blog(id)
#     title = f'{blog.title}'
#     reviews = Review.get_reviews(blog.id)

#     return render_template('blog.html',title = title,blog = blog,reviews = reviews)


# @app.route('/user/<uname>/update',methods = ['GET','POST'])
# # @login_required
# def update_profile(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)

#     form = UpdateProfile()

#     if form.validate_on_submit():
#         user.bio = form.bio.data

#         db.session.add(user)
#         db.session.commit()

#         return redirect(url_for('.profile',uname=user.username))

#     return render_template('profile/update.html',form =form)
