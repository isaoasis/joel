from flask import render_template, Blueprint, redirect, url_for
from page.views.admin import posts
from flask_login import login_user, logout_user, current_user 
from page.models.users import User 
from page.models.post import Post
from page import db
blog = Blueprint('blog', __name__)


@blog.route("/")
def index():
    posts = Post.get_all()  # Los posts ya están ordenados por get_all()
    return render_template("blog/index.html", posts=posts)

@blog.route("/p/<string:slug>/")
def show_post(slug):
    post = Post.get_by_slug(slug)
    if post is None:
        return "Este post no existe", 404  # Render a 404 page if the post is not found
    return render_template("blog/post_view.html", post=post)

@blog.route('/profile/<string:username>')
def user_profile(username):
    user = User.get_by_name(username)
    if user is None:
        return "Usuario no encontrado", 404
    
    # Obtener todos los posts y filtrar por autor
    user_posts = [post for post in Post.get_all() if post.author == user.name]
    
    return render_template("blog/profile.html", user=user, user_posts=user_posts)