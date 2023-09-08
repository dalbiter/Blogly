from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User model"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(35), nullable=False)
    last_name = db.Column(db.String(35), nullable=False)
    image_url = db.Column(db.Text, default='/static/images/default_profile_photo.png')

    def __repr__(self):
        u = self
        return f"User<User ID={u.id}, first name={u.first_name}, last name={u.last_name}, image={u.image_url}>"
    
    # add method for full name
    
class Post(db.Model):
    """Post model"""

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref='posts')

    def __repr__(self):
        p = self
        return f"Post<Post ID={p.id}, title={p.title}, content={p.content}, user_id={p.user_id}"
        # dont forget to add date to repr one figure our how to implement it