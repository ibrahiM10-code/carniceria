var correo = document.getElementById("correo");
var correoU = "{{correo}}";
var contraseñaU = "{{contraseña}}";

function validar(){ 
    if(correo.value == ""){
        alerta_invalida.classList.add("aparecer")
        correo.classList.add("borde_rojo");
        alerta_correo.classList.remove("aparecer");

        setTimeout(() => {
            alerta_correo.classList.add("desaparecer");
        },3000)

        alerta_correo.classList.remove("desaparecer");

        setTimeout(()=>{
            alerta_correo.classList.add("aparecer");
        },4000)
    }

    if(correo.value !== correoU || contraseña.value !== contraseñaU){
        
        alerta_invalida.classList.remove("aparecer");

        setTimeout(() => {
            alerta_invalida.classList.add("desaparecer");
        },3000)

        alerta_invalida.classList.remove("desaparecer");

        setTimeout(()=>{
            alerta_invalida.classList.add("aparecer");
        },4000)
    }

    if(contraseña.value == ""){
        alerta_invalida.classList.add("aparecer");
        contraseña.classList.add("borde_rojo");                    
        alerta_contraseña.classList.remove("aparecer");

        setTimeout(() => {
            alerta_contraseña.classList.add("desaparecer");
        },3000)

        alerta_contraseña.classList.remove("desaparecer");

        setTimeout(()=>{
            alerta_contraseña.classList.add("aparecer");
        },4000)
    }

    }


