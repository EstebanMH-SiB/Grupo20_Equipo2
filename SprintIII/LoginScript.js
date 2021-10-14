const bLogin = document.getElementById("bLogin");

const usuario = document.getElementById("userName");
const contraseña = document.getElementById("password");

const uWarning = document.getElementById("uWarning");
const cWarning = document.getElementById("pWarning");

function warnings(input, warning, msg, min, max) {
    var x = true;
    if (input.value == "") {
        warning.textContent = 'Este campo es obligatorio';
        x = false;
    } else {
        if (input.value.length < min || input.value.length > max) {
        warning.textContent = msg + ' no cumple con las caraterísticas. Intente nuevamente.';
        x = false;
        } else {
        warning.textContent = ""};
    }
    console.log(x);
    return x;
}

bLogin.addEventListener("click",function(evt){
    var registrar = false;

    var nValidation = warnings(usuario, uWarning, 'El usuario', 6, 30);
    var cValidation = warnings(contraseña, cWarning, 'La contraseña', 8, 16);

    if (nValidation && cValidation){
            registrar = true;
    };

    if (registrar == false) {
        console.log(evt);
        evt.preventDefault();
    } else {
        return true;
    }
})

function see_pword(eye, type){
    document.getElementById("peye").setAttribute("src", "../../icons/" + eye + ".svg");
    contraseña.setAttribute("type", type);
}