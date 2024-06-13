from flask import render_template, request, redirect, url_for, Blueprint
from page.forms import SignupForm, LoginForm

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        
        # Procesar el registro del usuario aquí (guardar en base de datos, etc.)

        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)
        return redirect(url_for('blog.index'))
    
    return render_template('auth/signup_form.html', form=form)

@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data

        # Procesar el login del usuario aquí (verificar en base de datos, etc.)

        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)
        return redirect(url_for('blog.index'))
    return render_template('auth/login_form.html', form=form)

    