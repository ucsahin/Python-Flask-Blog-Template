from setup import db, app, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

# necessary for login_manager to load current user
with app.app_context():
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, user_id)
    
# DEFINES the model classes initialized on the database
class User(db.Model, UserMixin):
    __tablename__ = 'users_table'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png')
    about_text = db.Column(db.String, nullable=False, default='All about me!')
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)

    blog_posts = db.relationship('BlogPost', backref='author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

class BlogPost(db.Model):
    __tablename__ = 'blog_posts_table'    

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    body_text = db.Column(db.String, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, title, body_text, user_id):
        self.title = title
        self.body_text = body_text
        self.user_id = user_id
    
    def update_creation_date(self, new_date):
        self.creation_date = new_date
