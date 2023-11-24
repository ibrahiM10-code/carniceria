const divCategoriaCarnes = document.querySelector(".categoria-vacuno");
const divCategoriaAves = document.querySelector(".categoria-aves");
const divSubCategoriasVacuno = document.querySelector(".sub-categorias-vacunos");
const divSubCategoriasAves = document.querySelector(".sub-categorias-aves");

divCategoriaCarnes.addEventListener("mouseover", () => {
    divSubCategoriasVacuno.style.display = "block"
});

divCategoriaCarnes.addEventListener("mouseout", () => {
    divSubCategoriasVacuno.style.display = "none";
});

divSubCategoriasVacuno.addEventListener("mouseover", () => {
    divSubCategoriasVacuno.style.display = "block";
});

divSubCategoriasVacuno.addEventListener("mouseout", () => {
    divSubCategoriasVacuno.style.display = "none";
});

divCategoriaAves.addEventListener("mouseover", () => {
    divSubCategoriasAves.style.display = "block";
});

divCategoriaAves.addEventListener("mouseout", () => {
    divSubCategoriasAves.style.display = "none";
});

divSubCategoriasAves.addEventListener("mouseover", () => {
    divSubCategoriasAves.style.display = "block";
});

divSubCategoriasAves.addEventListener("mouseout", () => {
    divSubCategoriasAves.style.display = "none";
});



function checkBtn() {
    const checkBoxCompra = document.getElementById("chkbx-compra");
    const btnCompra = document.getElementById("btn-pagar-ya");
    const checkBoxPreCompra = document.getElementById("chkbx-pre-compra");
    const btnPreCompra = document.getElementById("btn-pre-compra");
    const metodosPago = document.querySelector(".metodo-pago-container");
    
    if (checkBoxCompra.checked === true && checkBoxPreCompra.checked === true) {
        alert('Solo puede seleccionar un metodo de compra.');
        checkBoxCompra.checked = false;
        checkBoxPreCompra.checked = false;
        btnCompra.style.display = "none";
        btnPreCompra.style.display = "none";
        return false
    } else if (checkBoxCompra.checked == true) {
        btnCompra.style.display = "block";
        return true
    } else if (checkBoxPreCompra.checked == true) {
        btnPreCompra.style.display = "block";
        metodosPago.style.display = "none";
        return true
    } else if (checkBoxPreCompra.checked == false) {
        btnPreCompra.style.display = "none";
        metodosPago.style.display = "block";
        return false
    }

    if (checkBoxCompra.checked == false) {
        btnCompra.style.display = "none";
        return false
    }
}
