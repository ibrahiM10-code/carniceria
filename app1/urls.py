from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app1 import views as vista
#importamos las vistas desde la aplicacion
urlpatterns = [
    path('',vista.inicio,name='index'),
    path('carnes/',vista.carnes,name='carnes'),
    path('embutidos/',vista.embutidos,name='embutidos'),
    path('aves/',vista.aves,name='aves'),
    path('cerdo/',vista.cerdo,name='cerdo'),
    path('interiores/',vista.interiores,name='interiores'),
    path('cazuela/',vista.cazuela,name='cazuela'),
    path("miCarrito/", vista.lista_compras, name="carrito"),
    path("pavo/", vista.pavo, name="pavo"),
    path("detalles_compras/", vista.detalle_compra, name="detallesC"),   
    path("login_user/", vista.login_user, name="login"),
    path("logout_user", vista.logout_user, name="logout"),
    path("precompra/", vista.Precompra, name="precompra"),  
    path("registrarse/", vista.registrar_usuario, name="registro"),
    path("vista_producto/",vista.vista_producto,name="vista_producto"),
    path('vista_producto/carniApp1/lista_compras.html',vista.inicio,name='index'),
    path("resultados/", vista.resultado_busqueda, name="resultados"),
    path("recuperarClave/", vista.recuperar_clave, name="recuperarClave"),
    path("codigoRecuperacion/", vista.codigo_recuperacion, name="codigoRecuperacion"),
    path("cambioExitoso/", vista.cambio_exitoso, name="cambioExitoso"),
    path("create-order/", vista.create_order, name="crearOrden"),
    path("capture-order/", vista.capture_order, name="capturarOrden"),
    path("cancel-order/", vista.cancel_order, name="cancelarOrden"),
    path("del_producto_carrito/<int:idProducto>", vista.quitar_producto_carrito, name="quitarProducto")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)