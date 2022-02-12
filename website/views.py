from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/news')
@login_required
def news():
    return render_template("news.html", user=current_user)

@views.route('/projects')
@login_required
def projects():
    return render_template("projects.html", user=current_user)

@views.route('/about-me')
def about_me():
    return render_template("about_me.html", user=current_user)

@views.route('/impressum')
def impressum():
    return render_template("impressum.html", user=current_user)

@views.route('/credit')
def credit():
    return render_template("credit.html", user=current_user)