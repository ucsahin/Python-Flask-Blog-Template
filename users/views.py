from flask import render_template, Blueprint, redirect, url_for, flash, request, abort
from flask_login import login_user, login_required, logout_user, current_user
from setup import app, db
from models import User
from users.forms import RegisterForm, LoginForm, UpdateUserForm
from users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)

with app.app_context():

    # about user page view
    @users.route('/about/user_<int:user_id>', methods=['POST', 'GET'])
    @login_required
    def about(user_id):
        user = db.session.get(User, user_id)

        return render_template('about.html', user=user)
    
    @users.route('/update/user_<int:user_id>', methods=['POST', 'GET'])
    @login_required
    def update_about(user_id):
        user = db.session.get(User, user_id)

        # user can only edit her/his own accout
        if user != current_user:
            abort(403) # no authorization error

        form = UpdateUserForm()

        if form.validate_on_submit():

            if current_user.username != form.username.data:
                current_user.username = form.username.data

            if form.picture.data:
                username = current_user.username
                pic = add_profile_pic(form.picture.data, username)
                current_user.profile_image = pic
            
            current_user.about_text = form.about_text.data
            db.session.commit()

            flash('User Account Updated!')
            return redirect(url_for('users.about', user_id=current_user.id))

        form.username.data = current_user.username
        form.about_text.data = current_user.about_text
        
        return render_template('update_about.html', form=form)
        

    # register user page view
    @users.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()

        if form.validate_on_submit():
            user = User(email=form.email.data,
                        username=form.username.data,
                        password=form.password.data)

            db.session.add(user)
            db.session.commit()
            
            flash('Thanks for registration.')

            return redirect(url_for('users.login'))
        
        return render_template('register.html', form=form)

    # login user page view
    @users.route('/login', methods=['POST', 'GET'])
    def login():
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()

            if user is not None and user.check_password(form.password.data):
                login_user(user)
                flash('Log in Success!')

                next = request.args.get('next')

                if next == None or not next[0] == '/':
                    next = url_for('core.index')

                return redirect(next)
            
            else:
                flash("Username/password does not match!", "error")
            
        return render_template('login.html', form=form)

    # logout user page view
    @users.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for("core.index"))
