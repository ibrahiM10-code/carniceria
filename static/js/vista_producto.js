// Obtén el elemento span y el input por su id
var cantidadKilosSpan = document.querySelector(".cantidad-kilos");
var inputCantidad = document.getElementById("inputCantidad");
var precioElement = document.getElementById("precio"); // Agregamos esta línea para obtener el elemento del precio
var inputPrecio = document.getElementById("inputPrecio");

// Calcula el precio inicial y el precio por kilo
var precioInicial = parseFloat(precioElement.textContent.replace("$", ""));
var kilos = parseInt(inputCantidad.value);
var precioPorKilo = precioInicial / kilos;

// Agregar evento al botón de suma
document.querySelector(".btn-plus").addEventListener("click", function () {
    var valorActual = parseInt(cantidadKilosSpan.innerText);
    valorActual = isNaN(valorActual) ? 0 : valorActual;
    valorActual++;
    cantidadKilosSpan.innerText = valorActual;
    inputCantidad.value = valorActual;
    

    // Calcula el nuevo precio
    var nuevoPrecio = valorActual * precioPorKilo;
    precioElement.textContent = "$" + nuevoPrecio;
    inputPrecio.value = nuevoPrecio;
});

// Agregar evento al botón de resta
document.querySelector(".btn-menos").addEventListener("click", function () {
    var valorActual = parseInt(cantidadKilosSpan.innerText);
    valorActual = isNaN(valorActual) ? 0 : valorActual;
    if (valorActual > 1) {
        valorActual--;
        cantidadKilosSpan.innerText = valorActual;
        inputCantidad.value = valorActual;

        // Calcula el nuevo precio
        var nuevoPrecio = valorActual * precioPorKilo;
        precioElement.textContent = "$" + nuevoPrecio;
    }
});