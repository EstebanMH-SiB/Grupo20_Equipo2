const bRegistrar = document.getElementById("bRegistrar");

const nombre = document.getElementById("name");
const apellido = document.getElementById("surname");
const sexo = document.getElementById("sex");
const cumpleaños = document.getElementById("birthday");
const email = document.getElementById("email");
const usuario = document.getElementById("username");
const contraseña = document.getElementById("password");
const confirmarc = document.getElementById("pconfirmation");

const nWarning = document.getElementById("nameWarning");
const aWarning = document.getElementById("snameWarning");
const sWarning = document.getElementById("sexWarning");
const eWarning = document.getElementById("e-Warning");
const uWarning = document.getElementById("uWarning");
const cWarning = document.getElementById("pWarning");
const ccWarning = document.getElementById("pcWarning");
const TCWarning = document.getElementById("TCWarning")

const today = new Date();
var month = today.getUTCMonth() + 1;
var day = today.getUTCDate();
var year = today.getUTCFullYear();
maxdate = (year-18) + "-" + month + "-" + day;
cumpleaños.value = maxdate;
cumpleaños.setAttribute("max", maxdate);

const e_regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$/;
const u_regex = /^([^0-9]*|[^a-z]*)$/;
const p_regex = /^([^0-9]*|[^A-Z]*|[^a-z]*)$/;

function warnings(input, warning, msg) {
    var x = true;
    if (input.value == "") {
        warning.textContent = msg;
        x = false;
    } else {warning.textContent = ""};
    console.log(x);
    return x;
}

function warning_matches(input, regex, warning, msg) {
    var x = true;
    if (!input.value.match(regex)) {
        warning.textContent = msg + ' no cumple con las caraterísticas. Intente nuevamente.';
        x = false;
    } else {warning.textContent = ""};
    console.log(x + input +  " matches");
    return x;
}
function warning_wrongmatches(input, regex, warning, msg) {
    var x = true;
    if (input.value.match(regex)) {
        warning.textContent = msg + ' no cumple con las caraterísticas. Intente nuevamente.';
        x = false;
    } else {warning.textContent = ""};
    console.log(x + input +  " matches");
    return x;
}
function warning_length(input, min, max, warning, msg) {
    var x = true;
    if (input.value.length < min || input.value.length > max) {
        warning.textContent = msg + ' no cumple con las caraterísticas. Intente nuevamente.';
        x = false;
    } else {warning.textContent = ""};
    console.log(input.value.length)
    console.log(x + "lenght");
    return x;
}

bRegistrar.addEventListener("click",function(evt){
    var registrar = false;

    var nValidation = warnings(nombre, nWarning, 'Este campo es obligatorio');
    var aValidation = warnings(apellido, aWarning, 'Este campo es obligatorio');
    var sValidation = warnings(sexo, sWarning, 'Este campo es obligatorio');
    var ccValidation = warnings(confirmarc, ccWarning, 'Este campo es obligatorio');

    var uValidation = warning_wrongmatches(usuario, u_regex, uWarning, 'El usuario');
    var cValidation = warning_wrongmatches(contraseña, p_regex, cWarning, 'la contraseña');
    var uValidation2 = warning_length(usuario, 6, 30, uWarning, 'El usuario');
    var cValidation2 = warning_length(contraseña, 8, 12, cWarning, 'la contraseña');
    var eValidation = warning_matches(email, e_regex, eWarning, 'El correo electrónico');

    if (nValidation && aValidation && sValidation && ccValidation && 
        uValidation && cValidation && eValidation && uValidation2 && cValidation2){
            registrar = true;
    };

    if(!this.form.TeC.checked) {
        TCWarning.textContent = 'Este campo es obligatorio'; 
        registrar = false;
    } 
    else {
        TCWarning.textContent = "";
    };
    if(contraseña.value != "") { 
        if (confirmarc.value != contraseña.value) {
            ccWarning.textContent = 'Las contraseñas son distintas. Intente nuevamente.';
            registrar = false;
        };
    };

    if (registrar == false) {
        console.log(evt);
        evt.preventDefault();
    } else {
        return true;
    }
})

function mostrarReq(id, script) {
    var userRequisito = document.getElementById(id);
    userRequisito.innerHTML = script;
}

function changeMargin(px) {
    const after = document.getElementsByClassName("aftersex");
    for (var i = 0; i < after.length; i++) {
        after[i].setAttribute("style", "margin-top: " + px);
    };
}

function see_pword(eye, type){
    document.getElementById("peye").setAttribute("src", "/static/icons/" + eye + ".svg");
    contraseña.setAttribute("type", type);
}

function see_pcword(eye, type){
    document.getElementById("pceye").setAttribute("src", "/static/icons/" + eye + ".svg");
    confirmarc.setAttribute("type", type);
}