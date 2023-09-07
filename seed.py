"""Seed file with a few users and posts"""

from models import User, Post, db
from app import app
from datetime import datetime

#clear and re-create all tables
db.drop_all()
db.create_all()

u1 = User(first_name='Dan', last_name='Albiter', image_url='https://images.panda.org/assets/images/pages/welcome/orangutan_1600x1000_279157.jpg')
u2 = User(first_name='Cort', last_name='Albiter', image_url='https://img.freepik.com/premium-photo/dreamy-beach-paradise-landscape-vivid-colors_823696-2.jpg')
u3 = User(first_name='Test', last_name='User')
u4 = User(first_name='Test', last_name='User2')

p1 = Post(title='My First Post', content='This is the first post on my new app, pretty cool huh?', user_id=1)
p2 = Post(title='I love my fiance', content="When it comes to guys, I don't think I could have found a better man. He takes such good care of me", user_id=2)
p3 = Post(title='My Second Post', content='I wonder if anybody is actually reading this?', user_id=1)
p4 = Post(title='Test Post', content='This post is for the test user. Just making sure everything works =)', user_id=3)

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)

db.session.commit()

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)

db.session.commit()

