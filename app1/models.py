from django.db import models
from django.utils import timezone
import os

class Usuario(models.Model):
    rut = models.CharField(primary_key=True,max_length=10,verbose_name="RUT")
    nombre = models.CharField(max_length=50,verbose_name="Nombres")
    paterno = models.CharField(max_length=50,verbose_name="Apellido paterno")
    materno = models.CharField(blank=True,null=True, max_length=50,verbose_name="Apellido materno")
    numeroContacto = models.PositiveIntegerField(default=912345678,verbose_name="Numero de contacto")
    email = models.CharField(max_length=100,verbose_name="Correo del usuario")
    nombre_usuario = models.CharField(max_length=50, verbose_name="Nombre de usuario (distinto al nombre anterior)", unique=True)
    contraseña = models.CharField(max_length=100,verbose_name="Contraseña del usuario")
    fechaNaci = models.DateField(verbose_name="Fecha de nacimiento")
    creado = models.DateTimeField(default=timezone.now,editable=False)
    
    def __str__(self) -> str:
        return "{} {} {}".format(self.rut,self.nombre,self.paterno)
    
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['rut','nombre']

class Cajero(models.Model):
    rut = models.CharField(primary_key=True,max_length=10,verbose_name="RUT")
    nombre = models.CharField(max_length=50,verbose_name="Nombres")
    paterno = models.CharField(max_length=50,verbose_name="Apellido paterno")
    materno = models.CharField(blank=True,null=True, max_length=50,verbose_name="Apellido materno")
    numeroContacto = models.PositiveIntegerField(default=912345678,verbose_name="Numero de contacto")
    email = models.CharField(max_length=100,verbose_name="Correo del usuario")
    contraseña = models.CharField(max_length=100,verbose_name="Contraseña del usuario")
    fechaNaci = models.DateField(verbose_name="Fecha de nacimiento")
    fecha_contratacion = models.DateField(verbose_name="Fecha de contratacion", default=timezone.now)
    creado = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self) -> str:
        return "{} {} {} {}".format(self.rut,self.nombre,self.paterno, self.fecha_contratacion)
        
    class Meta:
        db_table = 'cajero'
        verbose_name = 'Cajero'
        verbose_name_plural = 'Cajeros'

class TipoProducto(models.Model):
    idTipoprod = models.BigAutoField(primary_key=True)
    nombreTipo = models.CharField(max_length=100,verbose_name="Nombre tipo producto")
    descripcionTipo = models.CharField(max_length=100, verbose_name="Descripción de la categoría")

    def generar_nombre(instance, filename):
        extension = os.path.splitext(filename)[1][1:]
        ruta = 'categorias'
        fecha = timezone.now().strftime("%d%m%Y_%H%M%S")
        nombre = f"{fecha}.{extension}"

        return os.path.join(ruta, nombre)
    
    fotoTipo = models.ImageField(upload_to=generar_nombre, null=True, blank=True, default='categorias/categoria.png')

    def __str__(self) -> str:
        return "{}".format(self.nombreTipo)
    
    class Meta:
        db_table = 'tipoProducto'
        verbose_name = 'TipoProducto'
        verbose_name_plural = 'TipoProductos'
    

class Producto(models.Model):
    idProducto = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100,verbose_name="Nombre del producto")
    marcaProduc = models.CharField(max_length=50,verbose_name="Nombre del producto")
    tipo = models.ForeignKey(TipoProducto,null=False,on_delete=models.RESTRICT)
    precio = models.PositiveIntegerField(default=100000,verbose_name="Precio del productos")
    descripcion = models.CharField(max_length=100, verbose_name="Descripción del producto", blank=True)
    kilage = models.IntegerField(verbose_name="Kilage", default=1)
    stock = models.IntegerField(verbose_name="Stock", default=1)
    descuento = models.IntegerField(verbose_name="Descuento", null=True, blank=True, default=0)
    
    def generar_nombre(instance, filename):
        extension = os.path.splitext(filename)[1][1:]
        ruta = 'productos'
        fecha = timezone.now().strftime("%d%m%Y_%H%M%S")
        nombre = f"{fecha}.{extension}"

        return os.path.join(ruta, nombre)

    imagenProduc = models.ImageField(upload_to=generar_nombre, null=True, default="productos/producto.png")

    def __str__(self) -> str:
        return "{} {} {}".format(self.idProducto,self.nombre,self.precio)
    
    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Carrito(models.Model):
    idProducto = models.BigAutoField(primary_key=True)
    nombre   = models.CharField(max_length=50,verbose_name="Nombre de producto", default="nombre")
    cantidad = models.PositiveIntegerField(default=10,verbose_name="Cantidad de productos")
    marcaProduc = models.CharField(max_length=50,verbose_name="Marca del producto")
    tipo_id = models.ForeignKey(TipoProducto,null=False,on_delete=models.CASCADE)
    precio = models.PositiveIntegerField(default=0,verbose_name="Precio del productos")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def generar_nombre(instance, filename):
        extension = os.path.splitext(filename)[1][1:]
        ruta = 'carrito'
        fecha = timezone.now().strftime("%d%m%Y_%H%M%S")
        nombre = f"{fecha}.{extension}"
        return os.path.join(ruta, nombre)

    imagen = models.ImageField(upload_to=generar_nombre, null=True, default="carro/carrito.png")
    
    def __str__(self) -> str:
        return "{}".format(self.nombre,self.marcaProduc,self.cantidad)
    
    class Meta:
        db_table = 'carrito'
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'

# Crear modelos Compra y Precompra.
class Compra(models.Model):
    fecha_compra = models.DateTimeField(default=timezone.now)
    total_compra = models.IntegerField(verbose_name="Total de la compra")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Cliente que realizo la compra")

    def __str__(self) -> str:
        return f"{self.id}-{self.fecha_compra}-{self.total_compra}-{self.usuario}"

    class Meta:
        db_table = "compra"
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

class PreCompra(models.Model):
    fecha_precompra = models.DateTimeField(default=timezone.now)
    total_precompra = models.IntegerField(verbose_name="Total de la precompra")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Cliente que realizo la precompra")
    estado = models.CharField(max_length=30,default="En espera")

    def __str__(self) -> str:
        return f"{self.fecha_precompra}-{self.total_precompra}-{self.estado}-{self.usuario}"

    class Meta:
        db_table = "precompra"
        verbose_name = "PreCompra"
        verbose_name_plural = "PreCompras"

# Crear modelos DetalleCompra y DetallePrecompra.
class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, verbose_name="Compra")
    nombre_producto = models.CharField(max_length=100)
    cantidad_comprada = models.CharField(max_length=10)
    precio_producto = models.IntegerField()
    imagen = models.CharField(max_length=150, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.nombre_producto}-{self.cantidad_comprada}-{self.precio_producto}-{self.imagen}"
    
    class Meta:
        db_table = "detalleCompra"
        verbose_name = "DetalleCompra"
        verbose_name_plural = "DetallesCompras"

class DetallePreCompra(models.Model):
    precompra = models.ForeignKey(PreCompra, on_delete=models.CASCADE, verbose_name="PreCompra")
    nombre_producto = models.CharField(max_length=100)
    cantidad_comprada = models.CharField(max_length=10)
    precio_producto = models.IntegerField()
    imagen = models.CharField(max_length=160)
    
    
    def __str__(self) -> str:
        return f"{self.nombre_producto}-{self.cantidad_comprada}-{self.precio_producto}-{self.imagen}"
    
    class Meta:
        db_table = "detallePreCompra"
        verbose_name = "DetallePreCompra"
        verbose_name_plural = "DetallesPreCompras"