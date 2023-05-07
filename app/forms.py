import random
import string

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

from .models import URLModel

class URLForm(FlaskForm):
    url = StringField("Вставьте ссылку", validators=[DataRequired(message="Поле не должно быть пустым"),
                                                     URL(message="Неверная ссылка")])
    submit = SubmitField("Получить короткую ссылку")

def get_short():
    while True:
        short = ''.join(random.choices(string.ascii_letters + string.ascii_letters, k=6))
        if URLModel.query.filter(URLModel.short == short).first():
            continue
        return short
