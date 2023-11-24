from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from app1.models import TipoProducto, Producto, Usuario
from app1.forms import CategoriaForm, ProductoForm, ClienteForm
from django.contrib.auth.decorators import permission_required

# Vista de la página del menu de los cruds.
def menu(request):
    return render(request, "crudsTemplates/menu_cruds.html")

# Vista del menú de categorías.
def categorias(request):
    categoria = TipoProducto.objects.all()
    return render(request, "crudsTemplates/catalogo.html", {"categorias": categoria})

# Vista del formulario para ingresar categorías.
# También muestra las categorías que existen.
@permission_required("app1.add_categoria")
def ingresar_categoria(request):
    categoria = TipoProducto.objects.all()
    cantidad_categorias = len(categoria)
    if request.method == "POST":
        form = CategoriaForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            print("Categoria agregada!")
            return redirect(reverse("catalogoCategorias"))
    else:
        form = CategoriaForm()
    
    return render(request, "crudsTemplates/ingresar_categorias.html", {"form": form, "categorias": categoria, "cantidad_categorias": cantidad_categorias})


# Vista para el formulario de edición de alguna categoría.
@permission_required("app1.edit_categoria")
def editar_categoria(request, idTipoprod):
    categoria = get_object_or_404(TipoProducto, idTipoprod=idTipoprod)

    if request.method == "POST":
        form = CategoriaForm(request.POST, request.FILES, instance=categoria)
        if form.is_valid():
            if "fotoTipo" in request.FILES:
                categoria.fotoTipo = request.FILES["fotoTipo"]
            form.save()
            return redirect(reverse("ingresarCategorias"))
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, "crudsTemplates/editar_categorias.html", {"form": form, "categorias": categoria})

# Vista para confirmar la eliminación de una categoría.
@permission_required("app1.delete_categoria")
def eliminar_categoria(request, idTipoprod):
    categoria = get_object_or_404(TipoProducto, idTipoprod=idTipoprod)
    if request.method == "POST":
        categoria.delete()
        return redirect(reverse("ingresarCategorias"))
    
    return render(request, "crudsTemplates/eliminar_categorias.html", {"categoria": categoria})

@permission_required("app1.edit_producto")
def editar_producto(request,idProducto):
    producto = get_object_or_404(Producto,idProducto=idProducto)
    form = ProductoForm(instance=producto)
    url = f"/panel-admin/lista_productos/{producto.tipo_id}"
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            if "foto" in request.FILES:
                producto.foto = request.FILES["foto"]
            form.save()
            return redirect(url)
    else:
        form = ProductoForm(instance=producto)
        
    productos = Producto.objects.all()    
    return render(request,'crudsTemplates/productoEdit.html',{'form':form,'productos':productos})
    
@permission_required("app1.delete_producto")
def eliminar_producto(request,idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    url = f"/panel-admin/lista_productos/{producto.tipo_id}"
    if request.method == 'POST':
        producto.delete()
        return redirect(url)
    
    return render(request,'crudsTemplates/productoDel.html',{'producto':producto})


# Vista para cargar un listado de productos de acuerdo a la categoria.
@permission_required("app1.view_product")
def productos_categoria(request, idTipoprod):
    categoria = get_object_or_404(TipoProducto, idTipoprod = idTipoprod)
    productos = Producto.objects.filter(tipo=idTipoprod)
    url = f"/panel-admin/lista_productos/{idTipoprod}"

    if request.method == 'POST': # nos aseguramos que estamos recibiendo una solicitud a través de un método POST
        form = ProductoForm(request.POST, request.FILES)# rescatamos los values del formulario
        print(request.POST, request.FILES)
        if form.is_valid():# verificamos que el formulario pase las validaciones
            form.save() # si las paso entonces guardamos
            messages.success(request, 'Registro exitoso')  # Agrega un mensaje de éxito
            return redirect(url)
    else:
        form = ProductoForm(initial={"descuento": 0})

    return render(request, "crudsTemplates/lista_productos.html", {"productos": productos, "categoria": categoria, "form": form, "cantidad_productos": len(productos)})


def resultados_busqueda(request, idTipoprod):

    if request.method == "POST":
        consulta = request.POST.get("consulta")
        productos = Producto.objects.filter(Q(nombre__icontains=consulta) | Q(marcaProduc__icontains=consulta) & Q(tipo=idTipoprod))
        cajeros = Usuario.objects.filter(Q(nombre__icontains=consulta) | Q(paterno__icontains=consulta) | Q(materno__icontains=consulta))
        return render(request, "crudsTemplates/resultados_busqueda.html", {"cantidad_productos": len(productos), "productos": productos, "cantidad_cajeros": len(cajeros), "cajeros": cajeros})
    else:
        return render(request, "crudsTemplates/resultados_busqueda.html", {})
    
@permission_required("app1.view_usuario")
def ingresar_cajero(request):
    usuario = Usuario.objects.all()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            print("Cajero agregado!")
            return redirect(reverse("ingresarCajero"))
    else:
        form = ClienteForm()

    return render(request, "crudsTemplates/ingresar_cajeros.html", {"form": form, "cajeros": usuario, "cantidad_cajeros": len(usuario)})

@permission_required("app1.edit_usuario")
def modificar_cajero(request, idUsuario):
    usuario = get_object_or_404(Usuario, rut=idUsuario)

    if request.method == "POST":
        form = ClienteForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect(reverse("ingresarCajero"))
    else:
        form = ClienteForm(instance=usuario)

    return render(request, "crudsTemplates/editar_cajero.html", {"form": form, "cajeros": usuario})

@permission_required("app1.delete_usuario")
def eliminar_cajero(request, idUsuario):
    usuario = get_object_or_404(Usuario, rut=idUsuario)

    if request.method == "POST":
        usuario.delete()
        return redirect(reverse("ingresarCajero"))
    
    return render(request, "crudsTemplates/eliminar_cajero.html", {"cajero": usuario})