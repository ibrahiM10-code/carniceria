from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, QueryDict
from django.urls import reverse
from app1 import models as datos
from app1.models import Carrito, Producto, Usuario, Compra, PreCompra, DetalleCompra, DetallePreCompra
from app1.forms import ClienteForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from requests.auth import HTTPBasicAuth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from dotenv import load_dotenv
import random, os, requests, json

# Carga las variables de entorno.
load_dotenv()

# Constantes necesarias para la API de Paypal.
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
API_SANDBOX = os.getenv("API_SANDBOX")
PORT = os.getenv("PORT")
DOLAR_API = 'https://mindicador.cl/api/dolar'

# Vista de la pagina principal
def inicio(request):
    return render(request, "carniApp1/index.html")

# Vista del login.
def login_user(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print("logged in")
            return redirect("/")
        else:
            print("error")
            messages.error(request, "Hubo un error, intentalo de nuevo.")
            return redirect("/login_user/")
    else:
        return render(request, 'registration/login.html')
    
def logout_user(request):
    logout(request)
    print("deslogueado!")
    redirect("index")

# Vista del registro de usuarios.
def registrar_usuario(request):
    if request.method == 'POST': # nos aseguramos que estamos recibiendo una solicitud a través de un método POST
        form = ClienteForm(request.POST)# rescatamos los values del formulario
        diccionario = {'csrfmiddlewaretoken': request.POST.get('csrfmiddlewaretoken'), 'username': request.POST.get('nombre_usuario'), 'password1': request.POST.get("contraseña"), 'password2': request.POST.get("reclave")}
        query_dict = QueryDict('', mutable=True)
        query_dict.update(diccionario)
        print(request.POST)
        print(query_dict)
        form2 = UserCreationForm(query_dict)
        print(form.is_valid(), form2.is_valid())
        print(form2.errors)
        if form.is_valid() and form2.is_valid(): # verificamos que el formulario pase las validaciones
            form.save() # si las paso entonces guardamos
            form2.save()
            username = form2.cleaned_data["username"]
            password = form2.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registro exitoso')  # Agrega un mensaje de éxito
            return redirect('index')
    else:
        form = ClienteForm()
    
    # retornamos renderizando al formulario que inicio lasolicitud
    return render(request,'carniApp1/registrar.html',{'form':form})

# Vista de los productos de cada categoria.
def carnes(request):
    if request.method == "GET" and "ordenar" in request.GET:
        # Ordenar productos de mayor a menor precio
        productos = {"producto": datos.carnesordeM}
    elif request.method == "GET" and "ordenar2" in request.GET:
        productos = {"producto": datos.carnesordeMe}
    else:
        # Mostrar productos sin ordenar
        productos = {"producto": datos.carnes}
    return render(request, "carniApp1/carne.html", productos)


def embutidos(request):
    if request.method == "GET" and "ordenar" in request.GET:
        # Ordenar productos de mayor a menor precio
        productos = {"producto": datos.embutidosordeM}
    elif request.method == "GET" and "ordenar2" in request.GET:
        productos = {"producto": datos.embutidosordeMe}
    else:
        # Mostrar productos sin ordenar
        productos = {"producto": datos.embutidos}
    return render(request, "carniApp1/embutidos.html", productos)


def aves(request):
    if request.method == "GET" and "ordenar" in request.GET:
      #  Ordenar productos de mayor a menor precio
        productos = {"producto": datos.avesMa}
    elif request.method == "GET" and "ordenar2" in request.GET:
        productos = {"producto": datos.avesMe}
    else:
        # Mostrar productos sin ordenar
        productosS = Producto.objects.filter(tipo_id=1)
        productos = {"producto": productosS}
    return render(request, "carniApp1/aves.html", productos)


def cerdo(request):
    if request.method == "GET" and "ordenar" in request.GET:
        # Ordenar productos de mayor a menor precio
        productos = {"producto": datos.cerdoMa}
    elif request.method == "GET" and "ordenar2" in request.GET:
        productos = {"producto": datos.cerdoMe}
    else:
        # Mostrar productos sin ordenar
        productos = {"producto": datos.cerdo}
    return render(request, "carniApp1/cerdo.html", productos)


def interiores(request):
    if request.method == "GET" and "ordenar" in request.GET:
        # Ordenar productos de mayor a menor precio
        productos = {"producto": datos.interioresMa}
    elif request.method == "GET" and "ordenar2" in request.GET:
        productos = {"producto": datos.interioresMe}
    else:
        # Mostrar productos sin ordenar
        productosS = Producto.objects.filter(tipo_id=7)
        productos = {"producto": productosS}
    return render(request, "carniApp1/cerdo.html", productos)


def cazuela(request):
    if request.method == "GET" and "ordenar" in request.GET:
        # Ordenar productos de mayor a menor precio
        productos = {"producto": datos.cazuelaMa}
    elif request.method == "GET" and "ordenar2" in request.GET:
        productos = {"producto": datos.cazuelaMe}
    else:
        # Mostrar productos sin ordenar
        productos = {"producto": datos.cazuela}
    return render(request, "carniApp1/cerdo.html", productos)


def pavo(request):
    if request.method == "GET" and "ordenar" in request.GET:
        # Ordenar productos de mayor a menor precio
        productos = {"producto": datos.pavoMa}
    elif request.method == "GET" and "ordenar2" in request.GET:
        productos = {"producto": datos.pavoMe}
    else:
        # Mostrar productos sin ordenar
        productosS = Producto.objects.filter(tipo_id=2)
        productos = {"producto": productosS}
    return render(request, "carniApp1/pavo.html", productos)

# Funcion para sumar precios de forma estatica.
# def suma_precios():
#     total = 0
#     for i in range(len(datos.ventas)):
#         total += datos.ventas[i]["precio"]
#     return total

# Vista para la lista de compras
# def lista_compras(request):
#     total_compra = suma_precios()
#     data = {"ventas": datos.ventas, "precio_final": total_compra}
#     return render(request, "carniApp1/lista_compras.html", data)

def lista_compras(request):
    usuario = get_object_or_404(Usuario, nombre_usuario=request.user)
    carrito_todo = Carrito.objects.filter(usuario=usuario)
    data = {"precio_final": 0,
            'carrito':carrito_todo}
    return render(request, "carniApp1/lista_compras.html", data)

def quitar_producto_carrito(request, idProducto):
    print(request.POST)
    if request.method == "POST":
        productoCarrito = get_object_or_404(Carrito, idProducto=idProducto)
        productoCarrito.delete()
        messages.success(request, "Producto eliminado del carrito!")
        return redirect('/miCarrito/')

# Vista para ver las compras realizadas.
def detalle_compra(request):
    usuario = get_object_or_404(Usuario, nombre_usuario=request.user)
    users_orders = Compra.objects.filter(usuario=usuario)
    print(users_orders)
    return render(request, "carniApp1/detalle_compra.html", {"carne1": datos.carnes1,"carne2": datos.carnes2,"cliente": datos.cliente, "users_orders": users_orders, "detalle_compra": DetalleCompra.objects.all()})


# Vista para ver las precompras realizadas.
def Precompra(request):
    usuario = get_object_or_404(Usuario, nombre_usuario=request.user)
    precompras_usuario = PreCompra.objects.filter(usuario=usuario)
    detalles_precompras = DetallePreCompra.objects.all()
    return render(request, "carniApp1/PreCompra.html", {"precompras_usuario": precompras_usuario, "detalles_precompras": detalles_precompras})

# Vista para visualizar un producto en singular.
def vista_producto(request):
    contador = request.GET.get('contador',None)
    codigo = request.GET.get('codigo', None)  # None es un valor predeterminado si 'codigo' no está presente
    imagen = request.GET.get('imagen',None)
    precio = request.GET.get('precio',None)
    nombre = request.GET.get('nombre',None)
    marca = request.GET.get('marca',None)
    tipo = request.GET.get('tipo',None)
    cantidad = request.GET.get('cantidad',None)
    if str(request.user) != "AnonymousUser" and str(request.user) != "ibrahim":
        usuario = get_object_or_404(Usuario, nombre_usuario=request.user)
        if tipo=="Vacuno":
            tipo=1
        else:
            pass

        if tipo=="Cerdo":
            tipo = 3
        else:
            pass

        if tipo=="Embutido":
            tipo=4
        else:
            pass

        if tipo=="Pollo":
            tipo=5
        else:
            pass

        if tipo=="Pavo":
            tipo=6
        else:
            pass

        producto = Carrito(
            nombre=nombre,
            cantidad=cantidad,
            marcaProduc=marca,
            tipo_id_id=tipo,
            precio=precio,
            imagen=imagen,
            usuario=usuario
        )

        if contador == "vacio":
            producto.save()
            messages.success(request, "Agregado al carrito correctamente!")

        respuesta = {
            'contador':contador,
            'codigo':codigo,
            'imagen':imagen,
            'precio':precio,
            'nombre':nombre,
            'marca':marca,
            'tipo':tipo,
        }
    else:
        print(request.user)
        respuesta = {
            'contador':contador,
            'codigo':codigo,
            'imagen':imagen,
            'precio':precio,
            'nombre':nombre,
            'marca':marca,
            'tipo':tipo,
        }


    return render(request,'carniApp1/vista_producto.html',respuesta)

def resultado_busqueda(request):
    productos = []
    if request.method == "GET":
        busqueda = request.GET.get("resultado")
        for id, embutido in datos.embutidos.items():
            if busqueda.lower() in embutido[0].lower():
                productos.append(embutido[0])
        for id, interior in datos.interiores.items():
            if busqueda.lower() in interior[0].lower():
                productos.append(interior[0])
        if len(productos) > 0:
            print(productos)
            return render(
                request,
                "resultados.html",
                {"result": busqueda, "embutidos": productos},
            )
    return render(request, "carniApp1/resultados.html", {})


def recuperar_clave(request):
    mensaje_error = False
    if request.method == "POST":
        mensaje_error = True
    return render(request, "carniApp1/recuperar_clave.html", {"mensaje_error": mensaje_error})


def codigo_recuperacion(request):
    if request.method == "POST":
        global clave1
        global clave2
        
        correo = request.POST.get("correo-cliente")
        clave1 = request.POST.get("clave-nueva")
        clave2 = request.POST.get("clave-nueva-repetida")
        code = random.randint(100000, 999999)
        request.session["code"] = code
        request.session["correo"] = correo
        request.session["clave1"] = clave1
        correo_usuario_db = Usuario.objects.filter(email=correo).values("email")[0].get("email")
        
        if correo == correo_usuario_db and clave1 == clave2:
            print("Code: {}".format(code))
            # with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as connection:
            #     connection.starttls()
            #     connection.login(user=DESDE_EMAIL, password=PSW_EMAIL)
            #     connection.sendmail(
            #         from_addr=DESDE_EMAIL,
            #         to_addrs=correo,
            #         msg=f"From: <{DESDE_EMAIL}> To: <{correo}> Subject: Verification Code!\n\nPsst... this is your code -> {code}",
            #     )
        elif correo != correo_usuario_db:
            messages.error(
                request,
                "Ha sucedido un error, verifique que el correo este escrito correctamente.",
            )
            return redirect(reverse("recuperarClave"))
        elif clave1 != clave2:
            messages.error(
                request, "Ha sucedido un error, verifique que las claves coincidan."
            )
            return redirect(reverse("recuperarClave"))

    return render(request, "carniApp1/confirmar_codigo.html")


def cambio_exitoso(request):
    if request.method == "POST":
        primer_numero = request.POST.get("primer-numero")
        segundo_numero = request.POST.get("segundo-numero")
        tercer_numero = request.POST.get("tercer-numero")
        cuarto_numero = request.POST.get("cuarto-numero")
        quinto_numero = request.POST.get("quinto-numero")
        sexto_numero = request.POST.get("sexto-numero")
        codigo_usuario_str = (
            primer_numero
            + segundo_numero
            + tercer_numero
            + cuarto_numero
            + quinto_numero
            + sexto_numero
        )
        code = request.session.get("code")
        correo = request.session.get("correo")
        print(code)
        codigo_usuario_int = int(codigo_usuario_str)
        if codigo_usuario_int != code:
            messages.error(request, "Los códigos no coinciden, inténtalo de nuevo.")
            return redirect(reverse("codigoRecuperacion"))
        else:
            print("logrado")
            user_nueva_clave = get_object_or_404(Usuario, email=correo)
            user_admin_nueva_clave = get_object_or_404(User, email=correo)
            print(user_admin_nueva_clave)
            user_nueva_clave.contraseña = clave1
            user_admin_nueva_clave.set_password(clave1)
            user_nueva_clave.save()
            user_admin_nueva_clave.save()

    return render(request, "carniApp1/cambio_exitoso.html")

# Funcion que genera el token de acceso a la API de Paypal.
def genera_access_token():
    access_token_headers = {"Content-Type": "application/x-www-form-urlencoded"}
    params = {"grant_type": "client_credentials"}
    access_token = requests.post(
            url=f"{API_SANDBOX}/v1/oauth2/token",
            headers=access_token_headers,
            params=params,
            auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
    )
    return access_token

#  Funcion que convierte los precios a dolares.
def a_dolar(lista_precios, dolar):
    precios_dolar = []
    for precio in lista_precios:
        precios_dolar.append(round(int(precio) / dolar))
    
    total = 0
    for precios in precios_dolar:
        total += precios

    return total

# Funcion que formatea el listado de compras.
def formatea_lista(cant_productos, nombre_productos, dolar, len_productos):
    total = 0
    items_list = []
    for i in range(0, len_productos):
        item = {"name": nombre_productos[i], "quantity": cant_productos[i], "unit_amount": {"currency_code": "USD", "value": round(Producto.objects.filter(nombre=nombre_productos[i]).values("precio")[0].get("precio") / dolar, 2)}}
        total += round(Producto.objects.filter(nombre=nombre_productos[i]).values("precio")[0].get("precio") / dolar, 2) * int(cant_productos[i])
        items_list.append(item) 
    return items_list, round(total, 2)

# Vista necesaria para crear la orden.
def create_order(request):
    global items_list, precio_final
    if len(request.POST.getlist("cantidadProductos")[0]) == 1:
        cantidades_de_productos = request.POST.getlist("cantidadProductos")
        precios = request.POST.getlist("precioPorProductos")
    elif len(request.POST.getlist("cantidadProductos")[0]) >  1 and len(request.POST.getlist("precioPorProductos"[0])) >  1:
        precios = request.POST.getlist("precioPorProductos")
        del precios[-2:]
        precios = precios[0].split(",")
        precios.pop(0)
        cantidades_de_productos = request.POST.getlist("cantidadProductos")
        del cantidades_de_productos[-2:]
        cantidades_de_productos = cantidades_de_productos[0].split(",")
        cantidades_de_productos.pop(0)
    elif len(request.POST.getlist("cantidadProductos")[0]) >  1:
        cantidades_de_productos = request.POST.getlist("cantidadProductos")
        cantidades_de_productos = cantidades_de_productos[0].split(",")
        cantidades_de_productos.pop(0)

   
    nombres_productos = request.POST.getlist("nombreProductos")
    productos = len(request.POST.getlist("nombreProductos"))
    checkbox_compra = request.POST.getlist("check-compra")
    checkbox_precompra = request.POST.getlist("check-precompra")
    precio_final = request.POST.getlist("precio_final")[0]

    response_dolar_api = requests.get(url=DOLAR_API)
    valor_dolar_actual = response_dolar_api.json()["serie"][0]["valor"]
    
    access_token = genera_access_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token.json()['access_token']}",
    }

    items_list, total = formatea_lista(cantidades_de_productos, nombres_productos, valor_dolar_actual, productos)

    data = {
        "intent": "CAPTURE",
        "purchase_units": [{"amount": {"currency_code": "USD", "value": total, "breakdown": {"item_total": {"currency_code": "USD", "value": total}}}, "items": items_list}],
        "payment_source": {
            "paypal": {
                "experience_context": {
                    "brand_name": "Donde xhe karlos",
                    "landing_page": "NO_PREFERENCE",
                    "user_action": "PAY_NOW",
                    "locale": "es-CL",
                    "return_url": f"{PORT}capture-order",
                    "cancel_url": f"{PORT}cancel-order",
                }
            }
        },
    }

    if checkbox_compra[0] == "on":
        global compra
        compra = 1
    elif checkbox_precompra[0] == "on":
        usuario_obj = get_object_or_404(Usuario, nombre_usuario=request.user)
        precompras = PreCompra.objects.create(total_precompra=request.POST.getlist("precio_final")[0], usuario=usuario_obj)
        for item in items_list:
            DetallePreCompra.objects.create(
                    precompra=precompras, nombre_producto=item["name"],
                    cantidad_comprada=item["quantity"], 
                    precio_producto=Producto.objects.filter(nombre=item["name"]).values("precio")[0].get("precio"),
                    imagen=Producto.objects.filter(nombre=item["name"]).values("imagenProduc")[0].get("imagenProduc")   
                )
        usuario = get_object_or_404(Usuario, nombre_usuario=request.user)
        Carrito.objects.filter(usuario=usuario).delete()
        return redirect("/precompra/")

    response_api_paypal = requests.post(
        url=f"{API_SANDBOX}/v2/checkout/orders",
        headers=headers,
        data=json.dumps(data),
    )

    print(response_api_paypal.json())

    return redirect(response_api_paypal.json()["links"][1]["href"])

# Vista necesaria para capturar la orden.
def capture_order(request):
    access_token = genera_access_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token.json()['access_token']}",
    }

    token = request.GET.get("token")
    response = requests.post(
        url=f"{API_SANDBOX}/v2/checkout/orders/{token}/capture", headers=headers
    )
    print(response.json())
    if response.status_code == 201 and compra == 1:
        usuario_obj = get_object_or_404(Usuario, nombre_usuario=request.user)
        compras = Compra.objects.create(total_compra=precio_final, usuario=usuario_obj)
        for item in items_list:
            DetalleCompra.objects.create(
                    compra=compras, nombre_producto=item["name"],
                    cantidad_comprada=item["quantity"], 
                    precio_producto=Producto.objects.filter(nombre=item["name"]).values("precio")[0].get("precio"),
                    imagen=Producto.objects.filter(nombre=item["name"]).values("imagenProduc")[0].get("imagenProduc")   
                )
        print("Compra hecha!")
        # Elimina los productos del carrito del usuario.
        usuario = get_object_or_404(Usuario, nombre_usuario=request.user)
        Carrito.objects.filter(usuario=usuario).delete()
        return redirect("/detalles_compras/")

# Vista necesaria para cancelar la orden.
def cancel_order(request):
    messages.error(request, "Ha habido un error al intentar la compra, intentalo de nuevo.")
    return redirect("/miCarrito/")