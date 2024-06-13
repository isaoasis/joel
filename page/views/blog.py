from flask import render_template, Blueprint, redirect, url_for
from page.views.admin import posts
from flask_login import login_user, logout_user, current_user 
from page.models.users import User
from page.views.auth import users
blog = Blueprint('blog', __name__)

def get_user_by_name(name):
    for user in users:
        if user.name == name:
            return user
    return None
@blog.route("/")
def index():
    sorted_posts = list(reversed(posts))
    return render_template("blog/index.html", posts=sorted_posts)

@blog.route("/p/<string:slug>/")
def show_post(slug):
    # Convert the slug and post title slugs to lowercase for comparison
    post = next((p for p in posts if p['title_slug'].lower() == slug.lower() or p['title'].lower() == slug.lower()), None)
    if post is None:
        return "Este post no existe", 404  # Render a 404 page if the post is not found

    return render_template("blog/post_view.html", post=post)

@blog.route('/profile/<string:username>')
def user_profile(username):
    user = get_user_by_name(username)
    if user is None:
        return "Usuario no encontrado", 404
    
    user_posts = [post for post in posts if post['author'] == user.name]
    # Sort user_posts in reverse order
    sorted_user_posts = list(reversed(user_posts))
    
    return render_template("blog/profile.html", user=user, user_posts=sorted_user_posts)
