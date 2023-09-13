"""Seed file with a few users and posts"""

from models import User, Post, db, Tag, PostTag
from app import app
from datetime import datetime

#clear and re-create all tables
db.drop_all()
db.create_all()

u1 = User(first_name='Dan', last_name='Albiter', image_url='https://images.panda.org/assets/images/pages/welcome/orangutan_1600x1000_279157.jpg')
u2 = User(first_name='Cort', last_name='Albiter', image_url='https://img.freepik.com/premium-photo/dreamy-beach-paradise-landscape-vivid-colors_823696-2.jpg')
u3 = User(first_name='Test', last_name='User')
u4 = User(first_name='Test', last_name='User2')

p1 = Post(title='My First Post', content='This is the first post on my new app, pretty cool huh?', created_at=datetime.now(), user_id=1)
p2 = Post(title='I love my fiance', content="When it comes to guys, I don't think I could have found a better man. He takes such good care of me", created_at=datetime.now(), user_id=2)
p3 = Post(title='My Second Post', content='I wonder if anybody is actually reading this?', created_at=datetime.now(), user_id=1)
p4 = Post(title='Test Post', content='This post is for the test user. Just making sure everything works. I also love puppies! =)', created_at=datetime.now(), user_id=3)
p5 = Post(title='Test Post nt', content='This post is for the test user. Just making sure everything works =)', created_at=datetime.now(), user_id=3)

t1 = Tag(name='Fun') 
         
t2 = Tag(name='Love') 
         
t3 = Tag(name='Puppies') 
    

pt1 = PostTag(post_id=1, tag_id=1)
pt2 = PostTag(post_id=2, tag_id=1)
pt3 = PostTag(post_id=3, tag_id=1)
pt4 = PostTag(post_id=2, tag_id=2)
pt5 = PostTag(post_id=4, tag_id=2)
pt6 = PostTag(post_id=4, tag_id=3)

# add seed users
db.session.add_all([u1, u2, u3, u4])

db.session.commit()

# add seed posts
db.session.add_all([p1, p2, p3, p4, p5])

db.session.commit()

#add seed tags
db.session.add_all([t1, t2, t3])

db.session.commit()

# add seed posts_tags
db.session.add_all([pt1, pt2, pt3, pt4, pt5, pt6])

db.session.commit()

