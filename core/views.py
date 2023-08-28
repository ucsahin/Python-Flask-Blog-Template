from flask import render_template, Blueprint
from setup import app, db
from models import BlogPost
from flask_login import current_user

core = Blueprint('core', __name__)

with app.app_context():

    # home page view --> displays blog posts after login
    @core.route('/')
    def index():
        all_posts = BlogPost.query.all()

        return render_template('index.html', blog_posts=all_posts)
