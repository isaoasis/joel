from flask import render_template, request, redirect, url_for, Blueprint
from page.models.users import User 
from page.models.forms import SignupForm, LoginForm
from page import login_manager
from flask_login import login_user, logout_user, current_user 
auth = Blueprint('auth', __name__, url_prefix='/auth')

users = [
    User(1, 'pepito', 'pepito@gmail.com', '1234'),
    User(2, 'juan', 'juan@gmail.com', '1234'),
    User(3, 'fulano', 'fulano@gmail.com', '1234'),
    User(4, 'mengano', 'mengano@gmail.com', '1234'),
]

def get_user(email):
    for user in users:
        if user.email==email:
            return user
        return None
    
@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        # Creamos el usuario y lo guardamos
        user = User(len(users) + 1, name, email, password)
        users.append(user)
        # Dejamos al usuario logueado
        login_user(user, remember=True)
        next_page = request.args.get('next', None)
        if not next_page or url_for(next_page).netloc != '':
            next_page = url_for('blog.index')
        return redirect(next_page)
    return render_template("auth/signup_form.html", form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_for(next_page).netloc != '':
                next_page = url_for('blog.index')
            return redirect(next_page)
    return render_template('auth/login_form.html', form=form)
    

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('blog.index'))

