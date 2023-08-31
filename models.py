from flask_sqlalchemy import SQLAlchemy

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

    image_url = db.Column(db.Text, nullable=False)

    def __repr__(self):
        u = self
        return f"User<User ID={u.id}, first name={u.first_name}, last name={u.last_name}, image={u.image_url}>"