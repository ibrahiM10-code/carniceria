id_codigo = document.getElementById("codigo");
var valor_codigo = (id) =>{
    var codigo = Math.floor(Math.random() * 100000);
    id.value = codigo;    
}
valor_codigo(id_codigo);
