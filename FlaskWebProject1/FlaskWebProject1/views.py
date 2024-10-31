"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template 
from FlaskWebProject1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/teachersLogin')
def teachersLogin():
    """Renders the contact page."""
    app.logger.info('Navigating to teachersLogin page')
    return render_template(
        'teachersLogin.html',
        title='Teachers Account',
        year=datetime.now().year,
        message='Account page.'
    )


@app.route('/attendancePage')
def attendancePage():
    """Renders the attendance Page"""
    return render_template(
        'attendancePage.html',
        title='Attendance',
        year=datetime.now().year,
        message='Attendance Domain'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/sectionAdding')
def sectionAdding():
    """Renders the about page."""
    return render_template(
        'sectionAdding.html',
        title='Section Adding',
        year=datetime.now().year,
        message='Add a section.'
    )
