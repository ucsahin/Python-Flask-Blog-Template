from flask import Blueprint, render_template, url_for, request, redirect, flash, abort
from setup import app, db
from flask_login import current_user, login_required
from models import BlogPost
from blog_posts.forms import BlogPostForm
from datetime import datetime

blog_posts = Blueprint('blog_posts', __name__)

with app.app_context():

    # create blog post view
    @blog_posts.route('/create_post', methods=['GET', 'POST'])
    @login_required
    def create_blog_post():
        form = BlogPostForm()

        if form.validate_on_submit():
            blog_post = BlogPost(title=form.title.data, body_text=form.content.data, user_id=current_user.id)
            db.session.add(blog_post)
            db.session.commit()

            flash('Blog post created successfully.', 'blog_post')

            return redirect(url_for('core.index'))

        return render_template('create_blog_post.html', form=form)

    # view blog post view
    @blog_posts.route('/view/blog_post_<int:blog_post_id>', methods=['GET', 'POST'])
    @login_required
    def view_blog_post(blog_post_id):
        blog_post = db.session.get(BlogPost, blog_post_id)

        return render_template("view_blog_post.html", blog_post=blog_post)

    # edit blog post view
    @blog_posts.route('/edit/blog_post_<int:blog_post_id>', methods=['GET', 'POST'])
    @login_required
    def edit_blog_post(blog_post_id):
        blog_post = db.session.get(BlogPost, blog_post_id)

        # user can only edit his/her own blog posts
        if blog_post.author != current_user:
            abort(403) # no authorization error

        form = BlogPostForm()
            
        if form.validate_on_submit():
            blog_post.title = form.title.data
            blog_post.body_text = form.content.data
            blog_post.update_creation_date(datetime.utcnow())
            
            #update blog post in the database
            db.session.commit()
            flash('Blog post edited successfully.', 'blog_post')

            return redirect(url_for('blog_posts.view_blog_post', blog_post_id=blog_post.id))

        form.title.data = blog_post.title
        form.content.data = blog_post.body_text

        return render_template('create_blog_post.html', form=form)
    
    # delete blog post view
    @blog_posts.route('/delete/blog_post_<int:blog_post_id>', methods=['GET', 'POST'])
    @login_required
    def delete_blog_post(blog_post_id):
        blog_post = db.session.get(BlogPost, blog_post_id)
        
        # user can only delete his/her own blog posts
        if blog_post.author != current_user:
            abort(403) # no authorization error

        db.session.delete(blog_post)
        db.session.commit()

        flash('Blog post deleted successfully.', 'blog_post')

        return redirect(url_for('core.index'))

