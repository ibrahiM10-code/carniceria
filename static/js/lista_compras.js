 // Obtener los botones y elementos span de cantidad
// Obtener los botones de suma y resta, elementos span de cantidad y precios
var botonesSuma = document.getElementsByClassName("btn_suma");
var botonesResta = document.getElementsByClassName("btn_resta");
var elemento_precio = document.querySelectorAll('#Precio');
var elementoCantidad = document.querySelectorAll("#cantidad");
var inputPrecio = document.getElementById("inputPrecio");
var inputCantidad = document.getElementById("inputCantidad");
var precioTotal = document.getElementById("precioTotal");
var productos = document.getElementsByClassName("datos-producto");
var subtotal = document.getElementById("precioTotal");
var precios = [];
var cantidades = [];

elemento_precio.forEach(function (elemento){
    var precioTexto = elemento.innerText.replace('Precio: ','');
    var precioNumero = parseFloat(precioTexto);

    precios.push(precioNumero);
});

elementoCantidad.forEach(function (element){
    var cantidadTexto = element.innerText;
    var cantidadNumero = parseInt(cantidadTexto);
    cantidades.push(cantidadNumero);
})

cantidades.unshift(0);
precios.unshift(0);

var precio_total = 0;

for(i=0; i<precios.length; i++){
    precio_total += precios[i];
}

console.log("Precio total: " + precio_total);
subtotal.value = precio_total;
var total = document.getElementById("total");
total.innerText = "Total: " + precio_total;

// Agregar event listeners a los botones de suma
for (var i = 0; i < botonesSuma.length; i++) {
    botonesSuma[i].addEventListener("click", function (e) {
        var cantidadElement = this.nextElementSibling; // El elemento siguiente es el span de cantidad
        var kilosElement = this.parentElement.parentElement.querySelector(".datos-producto p:nth-child(2)");
        var precioElement = this.parentElement.parentElement.querySelector("#Precio");

        var cantidadActual = parseInt(cantidadElement.innerText) || 0;
        cantidadActual += 1;
        cantidadElement.innerText = cantidadActual;

        var kilos = parseFloat(kilosElement.innerText.split(":")[1].trim());
        kilos += 1;
        kilosElement.innerText = "Kilos: " + kilos;

        // Calcula el nuevo precio específico para el producto
        var precioInicial = parseFloat(precioElement.textContent.replace("Precio: ", ""));
        var nuevoPrecio = (precioInicial / (kilos - 1)) * kilos;
        precioElement.innerText = "Precio: " + nuevoPrecio;
        var total_precio = nuevoPrecio - precioInicial;
        precio_total = precio_total + total_precio;
        total.innerText = "Total: " + precio_total;
        precioTotal.value = precio_total;
        subtotal.value = precio_total;
        console.log(subtotal.value);

        for (let j = 1; j < precios.length + 1; j++) {
            if (e.target.id == j){
                precios[e.target.id] = nuevoPrecio;
                inputPrecio.value = precios;
                cantidades[e.target.id] = cantidadActual;
                inputCantidad.value = cantidades;
            }
        }
    });
}

// Agregar event listeners a los botones de resta (similar al código de suma)
for (var i = 0; i < botonesResta.length; i++) {
    botonesResta[i].addEventListener("click", function (e) {
        var cantidadElement = this.previousElementSibling; // El elemento anterior es el span de cantidad
        var kilosElement = this.parentElement.parentElement.querySelector(".datos-producto p:nth-child(2)");
        var precioElement = this.parentElement.parentElement.querySelector("#Precio");

        var cantidadActual = parseInt(cantidadElement.innerText) || 0;
        if (cantidadActual > 1) {
            cantidadActual -= 1;
            cantidadElement.innerText = cantidadActual;
            // inputCantidad.value = cantidadActual;
            var kilos = parseFloat(kilosElement.innerText.split(":")[1].trim());
            kilos -= 1;
            kilosElement.innerText = "Kilos: " + kilos;

            // Calcula el nuevo precio específico para el producto
            var precioInicial = parseFloat(precioElement.textContent.replace("Precio: ", ""));
            var nuevoPrecio = (precioInicial / (kilos + 1)) * kilos;
            precioElement.innerText = "Precio: " + nuevoPrecio;
            // inputPrecio.value = nuevoPrecio;
            var total_precio = precioInicial - nuevoPrecio;
            precio_total = precio_total - total_precio;
            total.innerText = "Total: " + precio_total;
            precioTotal.value = precio_total;
            subtotal.value = precio_total;
            console.log(subtotal.value);

            for (let j = 1; j < precios.length + 1; j++) {
                if (e.target.id == j){
                    precios[e.target.id] = nuevoPrecio;
                    inputPrecio.value = precios[e.target.id];
                    cantidades[e.target.id] = cantidadActual;
                    inputCantidad.value = cantidades;
                }
            }
        }   
    });
}

