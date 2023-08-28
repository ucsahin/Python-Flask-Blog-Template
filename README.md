# Python-Flask-Blog-Template
Simple flask blog template with Python, Flask, HTML, CSS, JS, Bootstrap 5.
It features the following:
  - User and BlogPost tables with Flask-SQLAlchemy and Flask-Migrate.
  - User authentication with Flask-Login.
  - Bootstrap 5 HTML, CSS, and JS elements with Flask-WTF forms.
  - Password security with Werkzeug library.
  - Profile image handling with PILLOW.
  - Error handling with common error codes: 403, 404, etc.

To install necessary packages:
```
$ pip install requirements.txt
```
In order to create the database and migrate it (On Windows):
```
$ set FLASK_APP=app.py
$ flask db init
$ flask db migrate -m "migration message"
$ flask db upgrade
```
(On Linux, MacOS):
```
$ export FLASK_APP=app.py
$ flask db init
$ flask db migrate -m "migration message"
$ flask db upgrade
```
To run the FLASK app on the terminal:
```
$ python3 app.py
```
Then go to http://127.0.0.1:5000 to preview demo site.
### Home page without login:
![home_wout_login](https://github.com/ucsahin/Python-Flask-Blog-Template/assets/20977694/a73f3ee9-cd20-4df5-8b4b-cd561bf3eb27)

### New user registration:
![register](https://github.com/ucsahin/Python-Flask-Blog-Template/assets/20977694/d5e570f8-3f6b-4e9a-b59e-26e71307a153)

### Login user:
![login](https://github.com/ucsahin/Python-Flask-Blog-Template/assets/20977694/efd2779d-e012-46f9-b1f1-567fbe7ad652)

### Home page after login with already created blog post cards by different users:
![home_with_login](https://github.com/ucsahin/Python-Flask-Blog-Template/assets/20977694/707b378f-6527-4d3d-be9c-5e4a55c044ac)

### Single blog post view:
![blog_post](https://github.com/ucsahin/Python-Flask-Blog-Template/assets/20977694/a3a84b19-bfaf-48ba-930d-cc8a45dc7d77)

### About user page:
![about_me](https://github.com/ucsahin/Python-Flask-Blog-Template/assets/20977694/afb9dd1e-f58a-49f9-b587-1f729bae2f02)
