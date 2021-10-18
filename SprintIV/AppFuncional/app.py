import os
from flask import Flask, render_template, request, redirect, url_for
from utils import *
from forms import FormRegistro

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(30)


@app.route('/', methods=["GET",'POST'])
def index():
    return render_template('Home.html')    

@app.route('/AgregarVuelo', methods=["GET",'POST'])
def AgregarVuelo():
    return render_template('AgregarVuelo.html')

@app.route('/CambiarContraseña', methods=["GET",'PUT'])
def CambContraseña():
    return render_template('CambiarContraseña.html')

@app.route('/Comentarios', methods=["GET", "POST"])
def Comentarios():
    return render_template('ComentarioVuelos.html')

@app.route('/ConsultaVuelos', methods=['GET'])
def ConsultaVuelos():
    return render_template('ConsultaVuelo.html')

@app.route('/EdicionUsuario', methods=["GET",'PUT'])
def EdicionUsuario():
    return render_template('EdicionUsuario.html')

@app.route('/EditarUsuario', methods=["GET",'PUT'])
def EditarUsuario():
    return render_template('EditarUsuario.html')

@app.route('/EditarVuelo', methods=["GET",'PUT'])
def EditarVuelo():
    return render_template('EditarVuelo.html')

@app.route('/EliminarUser', methods=["GET",'DELETE'])
def EliminarUser():
    return render_template('EliminarUser.html')

@app.route('/EliminarVuelo', methods=["GET",'DELETE'])
def EliminarVuelo():
    return render_template('EliminarVuelo.html')

@app.route('/Home', methods=['GET','POST'])
def Home():
    return render_template('Home.html')

@app.route('/HomeAdministrador', methods=['GET','POST'])
def HomeAdministrador():
    return render_template('HomeAdministradorLogueado.html')

@app.route('/HomePiloto', methods=['GET','POST'])
def HomePiloto():
    return render_template('HomePilotoLogueado.html')

@app.route('/HomeUser', methods=['GET','POST'])
def HomeUser():
    return render_template('HomeUsuarioLogueado.html')

@app.route('/InfoPiloto', methods=['GET'])
def InfoPiloto():
    return render_template('InformacionPiloto.html')

@app.route('/InfoUser', methods=['GET'])
def InfoUser():
    return render_template('InformacionUsuario.html')

@app.route('/ItinerarioVuelo', methods=['GET'])
def ItinerarioVuelo():
    return render_template('ItinerarioVuelo.html')

@app.route('/Login', methods=['POST','GET'])
def Login():
    return render_template('Login.html')

@app.route('/RecuperarContraseña', methods=["GET",'POST'])
def RecuperarContraseña():
    return render_template('RecuperarContraseña.html')

@app.route('/RegistroUsuario', methods=['GET','POST'])
def RegistroUsuario():
    if request.method == "GET":
        formulario = FormRegistro()
        return render_template('RegistroUsuario.html', form=formulario)
    else:
        formulario = FormRegistro(request.form)
        if formulario.validate_on_submit():
            return render_template('RegistroUsuario.html',mensaje="Registro exitoso.", form=formulario)
        return render_template('RegistroUsuario.html', mensaje="Registro inválido, compruebe los campos", form=formulario)


@app.route('/RegistroUsuarioAdmin', methods=['GET','POST'])
def RegistroUsuarioAdmin():
    return render_template('RegistroUsuarioSuperAdmin.html')

@app.route('/ReservaVuelo', methods=['GET','POST'])
def ReservaVuelo():
    return render_template('ReservaVuelo.html')
