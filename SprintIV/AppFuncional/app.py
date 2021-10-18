from flask import Flask, render_template, request, redirect, url_for
from utils import *
from forms import FormRegistro

app = Flask(__name__)

@app.route('/', methods=["GET",'POST'])
def index():
    return render_template('Home.html')    

@app.route('/AgregarVuelo', methods=["GET",'POST'])
def AgregarVuelo():
    return render_template('AgregarVuelo.html')

@app.route('/CambiarContraseña', methods=["GET",'PUT','POST'])
def CambContraseña():
    return render_template('CambiarContraseña.html')

@app.route('/Comentarios', methods=["GET",'PUT'])
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

@app.route('/EliminarVuelo', methods=["GET",'POST'])
def EliminarVuelo():
    return render_template('EliminarVuelo.html')

@app.route('/Home', methods=['GET','POST',"PUT"])
def Home():
    return render_template('Home.html')

@app.route('/HomeAdministrador', methods=['GET'])
def HomeAdministrador():
    return render_template('HomeAdministradorLogueado.html')

@app.route('/HomePiloto', methods=['GET'])
def HomePiloto():
    return render_template('HomePilotoLogueado.html')

@app.route('/HomeUser', methods=['GET'])
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
            return render_template('RegistroUsuario.html')
    else:
        if request.form:
            nombre = request.form['nombre']
            usuario = request.form['usuario']
            sexo = request.form['sexo']
            email = request.form['email']
            contrasena = request.form['contrasena']
            declaracion = request.form['declaracion']

            errores = ""
            exito = ""

            if len(nombre) <= 0:
                errores+= "Debe escribir un nombre válido. "
            
            if not isUsernameValid(usuario):
                errores+= "Debe escribir un nombre de usuario válido. "
            
            if not isEmailValid(email):
                errores+= "Debe escribir un email válido. "
            
            if not isPasswordValid(contrasena):
                errores+= "La contraseña no cumple con los requisitos de seguridad. "
            
            if declaracion != "S":
                errores+= "Debe aceptar los terminos legales. "

            if not errores:
                exito = "Su cuenta ha sido registrada"
                return redirect(url_for('login'))
            else:
                return render_template('registro.html', error=errores)

@app.route('/RegistroUsuarioAdmin', methods=['GET','POST'])
def RegistroUsuarioAdmin():
    return render_template('RegistroUsuarioSuperAdmin.html')

@app.route('/ReservaVuelo', methods=['GET'])
def ReservaVuelo():
    return render_template('ReservaVuelo.html')
