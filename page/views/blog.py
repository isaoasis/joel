from flask import render_template, Blueprint, redirect, url_for
from page.views.admin import posts

blog = Blueprint('blog', __name__)

@blog.route("/")
def index():
    posts.reverse()
    return render_template("blog/index.html", posts=posts)


@blog.route("/p/<string:slug>/")
def show_post(slug):
    # Convertir el slug y los title_slug de los posts a minúsculas para comparar
    post = next((p for p in posts if p['title_slug'].lower() == slug.lower() or p['title'].lower() == slug.lower()), None)
    if post is None:
        return "Este post no existe", 404  # Renderiza una página 404 si el post no se encuentra

    return render_template("blog/post_view.html", post=post)