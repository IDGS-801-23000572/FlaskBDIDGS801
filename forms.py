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
    apellidos=StringField('apellidos',[
        validators.DataRequired(message="El apellido es requerido"),
    ])
    email=EmailField('correo',[
        validators.DataRequired(message="El correo es requerido"),
        validators.Email( message="Ingrese un correo válido"),
    ])
    telefono=StringField('telefono',[
        validators.DataRequired(message="El telefono es requerido")
    ])
    
class UserForm3(Form):
    matricula=IntegerField('matricula',[
        validators.NumberRange(min=1, max=20, message="valor no valido")
    ])
    nombre=StringField('nombre',[
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=4, max=20, message="Requiere minimo de 4 y maximo de 20"),
    ])
    apellidos=StringField('apellidos',[
        validators.DataRequired(message="El apellido es requerido"),
    ])
    especialidad=StringField('especialidad',[
        validators.DataRequired(message="La especialidad es requerido"),
    ])
    email=EmailField('correo',[
        validators.DataRequired(message="El correo es requerido"),
        validators.Email( message="Ingrese un correo válido"),
    ])
    