
fecha1 = document.getElementById("fecha");
fecha1 = document.getElementById("fecha2");

var hora = (id) =>{
    var fecha_actual = new Date().toLocaleDateString();
    id.textContent = fecha_actual;
}
hora(fecha);
hora(fecha2);



