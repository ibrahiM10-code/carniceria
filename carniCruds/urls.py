from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("menu/", views.menu, name="menuCruds"),
    path("catalogo-categorias/", views.categorias, name="catalogoCategorias"),
    path("ingresar-categoria/", views.ingresar_categoria, name="ingresarCategorias"),
    path("editar-categoria/<int:idTipoprod>", views.editar_categoria, name="editarCategoria"),
    path("eliminar-jugador/<int:idTipoprod>", views.eliminar_categoria, name="eliminarCategoria"),
    path("productoEdit/<int:idProducto>/",views.editar_producto,name="editarProducto"),
    path("eliminar_producto/<int:idProducto>/",views.eliminar_producto,name='eliminarProducto'),
    path("lista_productos/<int:idTipoprod>", views.productos_categoria, name="productosDeCategoria"),
    path("resultados/<int:idTipoprod>", views.resultados_busqueda, name="resultados"),
    path("ingresar_cajero/", views.ingresar_cajero, name="ingresarCajero"),
    path("modificar_cajero/<str:idUsuario>", views.modificar_cajero, name="modificarCajero"),
    path("eliminar_cajero/<str:idUsuario>", views.eliminar_cajero, name="eliminarCajero")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)