# page/views/admin.py
from flask import render_template, Blueprint, redirect, url_for, request
from flask_login import login_required, current_user
from page.models.forms import PostForm
from page.models.post import Post

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@admin.route("/post/<int:post_id>/", methods=['GET', 'POST'])
@login_required
def post_form(post_id):
    if post_id:
        post = Post.query.get_or_404(post_id)
        if post.user_id != current_user.id:
            return redirect(url_for('blog.index'))  # Redirect if the user is not the owner
    else:
        post = Post(user_id=current_user.id)

    form = PostForm(obj=post)
    if form.validate_on_submit():
        form.populate_obj(post)
        post.save()
        return redirect(url_for('blog.index'))
    
    return render_template("admin/post_form.html", form=form)
