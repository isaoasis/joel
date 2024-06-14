from flask import render_template, Blueprint, redirect, url_for
from page.models.forms import PostForm
from flask_login import login_required, current_user
import re  # Importa el módulo re para usar expresiones regulares

admin = Blueprint('admin', __name__, url_prefix='/admin')

posts = [
    {
        'title': 'Primer Post',
        'title_slug': 'primer-post',
        'content': 'Bienvenidos a mi blog personal. Este es el primer post donde compartiré mis pensamientos y experiencias.Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.',
        'author': 'mengano'
    },
    {
        'title': 'Python y Flask',
        'title_slug': 'python-flask',
        'content': 'Python es un lenguaje de programación muy versátil. Flask es un microframework que te permite crear aplicaciones web de forma rápida y sencilla.Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.',
        'author': 'fulano'
    },
    {
        'title': 'Desarrollo Web Moderno',
        'title_slug': 'desarrollo-web-moderno',
        'content': 'El desarrollo web ha evolucionado mucho en los últimos años. Tecnologías como React, Vue.js y frameworks como Flask y Django son muy populares.Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemplo "Contenido aquí, contenido aquí". Estos textos hacen parecerlo un español que se puede leer. Muchos paquetes de autoedición y editores de páginas web usan el Lorem Ipsum como su texto por defecto, y al hacer una búsqueda de "Lorem Ipsum" va a dar por resultado muchos sitios web que usan este texto si se encuentran en estado de desarrollo. Muchas versiones han evolucionado a través de los años, algunas veces por accidente, otras veces a propósito (por ejemplo insertándole humor y cosas por el estilo).Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.',
        'author': 'juan'
    },
    {
        'title': 'Data Science y Machine Learning',
        'title_slug': 'data-science-machine-learning',
        'content': 'El campo de la ciencia de datos y el aprendizaje automático está en auge. Python, con sus bibliotecas como Pandas y Scikit-learn, es una herramienta fundamental.Hay muchas variaciones de los pasajes de Lorem Ipsum disponibles, pero la mayoría sufrió alteraciones en alguna manera, ya sea porque se le agregó humor, o palabras aleatorias que no parecen ni un poco creíbles. Si vas a utilizar un pasaje de Lorem Ipsum, necesitás estar seguro de que no hay nada avergonzante escondido en el medio del texto. Todos los generadores de Lorem Ipsum que se encuentran en Internet tienden a repetir trozos predefinidos cuando sea necesario, haciendo a este el único generador verdadero (válido) en la Internet. Usa un diccionario de mas de 200 palabras provenientes del latín, combinadas con estructuras muy útiles de sentencias, para generar texto de Lorem Ipsum que parezca razonable. Este Lorem Ipsum generado siempre estará libre de repeticiones,Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur.Nulla accumsan augue vel turpis efficitur, vitae facilisis nisi tempus. Nulla dignissim, metus ac dapibus blandit, risus erat interdum lectus, venenatis efficitur lacus metus vitae ante. Cras feugiat diam in neque vestibulum, at varius nunc sagittis. Praesent ut lectus magna. In sed ligula dignissim, ornare sapien nec, luctus lorem. Mauris efficitur dolor est, iaculis scelerisque ipsum semper in. Proin nulla mauris, consectetur in mollis sed, iaculis a diam. Nullam bibendum, mi at consequat molestie, tellus metus scelerisque orci, sit amet tincidunt orci eros a nisl. Nam vitae accumsan diam. Aliquam dignissim felis sed sapien rhoncus auctor. Mauris auctor, lacus at ultrices interdum, neque nunc tempor ligula, quis ultricies nisi lorem sed justo. Fusce rutrum sagittis tellus, vitae posuere tellus interdum sed. Phasellus quis orci sed lorem accumsan consectetur. ',
        'author': 'pepito'
    },
]

def convert_to_slug(title):
    # Usa expresiones regulares para reemplazar espacios con guiones y convierte todo a minúsculas
    return re.sub(r'\s+', '-', title).lower()

@admin.route("/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@admin.route("/post/<string:post_id>/", methods=['GET', 'POST'])
@login_required
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        title_slug = convert_to_slug(form.title_slug.data) # Llama a la función para obtener el title_slug
        content = form.content.data
        author = current_user.name if current_user.is_authenticated else "Invitado"
        post = {'title': title, 'title_slug': title_slug, 'content': content, 'author': author}
        posts.append(post)
        return redirect(url_for('blog.index'))
    return render_template("admin/post_form.html", form=form)
