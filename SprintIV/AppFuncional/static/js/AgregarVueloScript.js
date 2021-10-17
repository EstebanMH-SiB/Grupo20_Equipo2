const bCrear = document.getElementById("bCrear");

const IDvuelo = document.getElementById("vuelo");
const origen = document.getElementById("origen");
const destino = document.getElementById("destino");
const dia = document.getElementById("departure-D");
const hora = document.getElementById("departure-H");
const piloto = document.getElementById("pilotName");
const IDpiloto = document.getElementById("pilotID");
const IDavion = document.getElementById("airplane");

const vWarning = document.getElementById("vWarning");
const oWarning = document.getElementById("orgWarning");
const dWarning = document.getElementById("desWarning");
const pWarning = document.getElementById("npWarning");
const ipWarning = document.getElementById("cpWarning");
const iaWarning = document.getElementById("capWarning");

const today = new Date();

var month = today.getUTCMonth() + 1;
var day = today.getUTCDate();
var year = today.getUTCFullYear();
date = year + "-" + month + "-" + day;

var hour = today.getHours();
var minutes = today.getMinutes();
time = hour + ":" + minutes;

dia.value = date;
hora.value = time;

function warnings(input, warning) {
    var x = true;
    if (input.value == "") {
        warning.textContent = "Este campo es obligatorio";
        x = false;
    } else {warning.textContent = ""};
    console.log(x);
    return x;
}

bCrear.addEventListener("click",function(evt){
    var registrar = false;

    var vValidation = warnings(IDvuelo, vWarning);
    var oValidation = warnings(origen, oWarning);
    var dValidation = warnings(destino, dWarning);
    var pValidation = warnings(piloto, pWarning);
    var ipValidation = warnings(IDpiloto, ipWarning);
    var iaValidation = warnings(IDavion, iaWarning);

    if (vValidation && oValidation && dValidation &&
        pValidation && ipValidation && iaValidation){
            registrar = true;
    };

    if (registrar == false) {
        console.log(evt);
        evt.preventDefault();
    } else {
        return true;
    }
})