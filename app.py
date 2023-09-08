from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import text
from models import db, connect_db, User, Post
from datetime import datetime

app = Flask(__name__)

app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_db'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'secret-key'
app.config['DEBUG_TB_INTERECEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

db.create_all()

@app.route('/')
def home_page():
    """at the moment redirects to users landing page"""

    return redirect('/users')

@app.route('/users')
def users():
    """Show list of current users"""

    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/users/new')
def add_new_user():
    """show create user form"""

    return render_template('new_users.html')

@app.route('/users/new', methods=['POST'])
def submit_new_user():
    """collects form data and submits new user, updates user table"""

    first = request.form['first_name']
    last = request.form['last_name']
    img = request.form['img_url']
    img = img if img else '/static/images/default_profile_photo.png'
   
    new_user = User(first_name=first, last_name=last, image_url=img)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user_details(user_id):
    """show user profile"""
    
    user = User.query.get_or_404(user_id)
    posts = user.posts
    print(user.image_url)
    return render_template('user_profile.html', user=user, posts=posts)

@app.route('/users/<int:user_id>/edit')
def edit_user_form(user_id):
    """show form to edit a user"""
    # need to refactor to db.session.get(User, user_id)
    user = User.query.get(user_id)
    return render_template('edit_user.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def edit_user(user_id):
    """takes user data from form and update database with new info"""

    user = User.query.get(user_id)
    first = request.form['first_name']
    first = first if first else user.first_name
    last = request.form['last_name']
    last = last if last else user.last_name
    img = request.form['img_url']
    img = img if img else user.image_url 

    user.first_name = first
    user.last_name = last
    user.image_url = img

    db.session.add(user)
    db.session.commit()

    print(img)

    return redirect(f'/users/{user_id}')

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """deletes current user from database"""

    User.query.filter_by(id=user_id).delete()

    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>/posts/new')
def new_post_form(user_id):
    """show form to add new post for current user"""

    user = db.session.get(User, user_id)
    return render_template('/new_post.html', user=user)

######################################################################################


@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def add_new_post(user_id):
    """takes form data and creates post for current user"""

    user = db.session.get(User, user_id)
    title = request.form['title']
    content = request.form['content']

    new_post = Post(title=title, content=content, created_at=datetime.now(), user_id=user_id)

    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/users/{user_id}')

@app.route('/posts/<int:post_id>')
def show_posts(post_id):
    """show post details for selected post"""
    
    post = db.session.get(Post, post_id)
    return render_template('post_details.html', post=post)

@app.route('/posts/<int:post_id>/edit')
def edit_post_form(post_id):
    """show edit post form"""

    post = db.session.get(Post, post_id)
    return render_template('edit_post.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def edit_post(post_id):
    """take form data and edti post"""

    post = db.session.get(Post, post_id)
    title = request.form['title']
    title = title if title else post.title
    content = request.form['content']
    content = content if content else post.content

    post.title = title
    post.content = content

    db.session.add(post)
    db.session.commit()
    return redirect(f'/posts/{post.id}')

@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    """deletes selected post from page and from database"""

    post = db.session.get(Post, post_id)
    user_id = post.user.id
    Post.query.filter_by(id=post_id).delete()
    
    db.session.commit()
    return redirect(f'/users/{user_id}')
