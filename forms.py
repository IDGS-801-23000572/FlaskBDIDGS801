from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, FloatField
from wtforms import EmailField
from wtforms import validators

class UserForm2(Form):
    id=IntegerField('id',
    [validators.NumberRange(min=1, max=20, message="valor no valido")])
    nombre=StringField('nombre',[
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=4, max=20, message="Requiere minimo de 4 y maximo de 20"),
    ])
    apaterno=StringField('apaterno',[
        validators.DataRequired(message="El apellido es requerido"),
    ])
    email=EmailField('correo',[
        validators.DataRequired(message="El correo es requerido"),
        validators.Email( message="Ingrese un correo válido"),
    ])