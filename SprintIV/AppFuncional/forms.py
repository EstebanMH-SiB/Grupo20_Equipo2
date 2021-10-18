import abc
from re import A
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField, TextAreaField

class FormContactanos(FlaskForm):
    nombre = StringField('Nombre Completo', validators=[validators.required(), validators.length(max=100)]) 
    correo = StringField('Correo Electrónico', validators=[validators.required(), validators.length(max=150)])
    mensaje = TextAreaField('Mensaje', validators=[validators.required(), validators.length(max=500)])
    enviar = SubmitField('Enviar Mensaje')

class FormRegistro(FlaskForm):
    name = StringField('Nombres',validators=[validators.required()])
    usuario = StringField('Usuario', validators=[validators.required(), validators.length(max=50) ])
    nombre = StringField('Nombre Completo', validators=[validators.required(), validators.length(max=100)])
    correo = StringField('Correo Electrónico', validators=[validators.email(), validators.length(max=150)])
    contrasena = PasswordField('Contraseña', validators=[validators.required(), validators.length(max=20, min=8)])
    
    enviar = SubmitField('Registrar')


    #nombre
    #apellido
    #sexo
    #fecha
    #correo
    #usuario
    #contraseña
    #confirmar contrasena





'''
    from models import usuario

class FormLogin(FlaskForm):
    usuario = StringField('Usuario', validators=[validators.required()])
    contrasena = PasswordField('Contraseña',validators=[validators.required()])
    enviar = SubmitField('Iniciar sesión')

class FormContactanos(FlaskForm):
    nombre = StringField('Nombre Completo', validators=[validators.required(), validators.length(max=100)]) 
    correo = StringField('Correo Electrónico', validators=[validators.required(), validators.length(max=150)])
    mensaje = TextAreaField('Mensaje', validators=[validators.required(), validators.length(max=500)])
    tipo = RadioField('Tipo de Mensaje', choices=[('P','Pregunta'),('Q','Queja'),('S','Sugerencia')])
    enviar = SubmitField('Enviar Mensaje')

class FormRespuesta(FlaskForm):
    nombre = StringField('Nombre Completo', validators=[validators.required(), validators.length(max=100)]) 
    correo = StringField('Correo Electrónico', validators=[validators.required(), validators.length(max=150)])
    mensaje_original = TextAreaField('Mensaje Original', validators=[validators.required(), validators.length(max=500)])
    respuesta = TextAreaField('Respuesta', validators=[validators.required(), validators.length(max=500)])
    enviar = SubmitField('Enviar Respuesta')

#WTForms para registro de usuarios
class FormRegistro(FlaskForm):
    usuario = StringField('Usuario', validators=[validators.required(), validators.length(max=50) ])
    nombre = StringField('Nombre Completo', validators=[validators.required(), validators.length(max=100)])
    correo = StringField('Correo Electrónico', validators=[validators.email(), validators.length(max=150)])
    contrasena = PasswordField('Contraseña', validators=[validators.required(), validators.length(max=20, min=8)])
    enviar = SubmitField('Registrar')
    '''