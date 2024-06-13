#IMPORTAR TODO SOBRE FORMULARIOS
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length 


#REGISTRAR USUARIO WTFORMS
class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=55)])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar usuario')
#LOGEAR UN USUARIO
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Iniciar Sesión')
#REGISTRAR UN POST
class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    title_slug = StringField('Título slug', validators=[Length(max=128)])
    content = TextAreaField('Contenido')
    submit = SubmitField('Publicar')