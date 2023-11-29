from django.db import models
from django.utils import timezone
from app1.choices import estado_precompra
import os
# Create your models here.

carnes = {
    101:['Huachalomo','Cat.V','Vacuno',9900,'huachalomo.png'],
    102:['Molida Especial','Cat.V','Vacuno',10500,'molida.png'],
    103:['Carne Picada','Cat.V','Vacuno',10500,'picada.png'],
    104:['Posta Negra','Cat.V','Vacuno',10800,'postaN.png'],
    105:['Posta Rosada','Cat.V','Vacuno',10800,'postaR.png'],
    106:['Posta Paleta','Cat.V','Vacuno',10990,'postaP.png'],
    107:['Abastero','Cat.V','Vacuno',9900,'abastero.png'],
    108:['Carnicero','Cat.V','Vacuno',9900,'carnicero.png'],
    109:['Sobrecostilla','Cat.V','Vacuno',9900,'sobrecostilla.png'],
    110:['Punta Paleta','Cat.V','Vacuno',11200,'puntaP.png'],
    111:['Tapabarriga','Cat.V','Vacuno',15900,'tapabarriga.png'],
    112:['Entraña','Cat.V','Vacuno',15900,'entraña.png'],
    113:['Palanca','Cat.V','Vacuno',14500,'palanca.png'],
    114:['Filete','Cat.V','Vacuno',15600,'filete.png'],
    115:['Asiento','Cat.V','Vacuno',12500,'asiento.png'],
    116:['Tapapecho','Cat.V','Vacuno',8900,'tapapecho.png'],
    117:['Lomo Vetado','Cat.V','Vacuno',12900,'lomovetado.png'],
}
carnesordeM = {
    112:['Entraña','Cat.V','Vacuno',15900,'entraña.png'],
    111:['Tapabarriga','Cat.V','Vacuno',15900,'tapabarriga.png'],
    114:['Filete','Cat.V','Vacuno',15600,'filete.png'],
    113:['Palanca','Cat.V','Vacuno',14500,'palanca.png'],
    117:['Lomo Vetado','Cat.V','Vacuno',12900,'lomovetado.png'],
    115:['Asiento','Cat.V','Vacuno',12500,'asiento.png'],
    110:['Punta Paleta','Cat.V','Vacuno',11200,'puntaP.png'],
    106:['Posta Paleta','Cat.V','Vacuno',10990,'postaP.png'],
    105:['Posta Rosada','Cat.V','Vacuno',10800,'postaR.png'],
    104:['Posta Negra','Cat.V','Vacuno',10800,'postaN.png'],
    102:['Molida Especial','Cat.V','Vacuno',10500,'molida.png'],
    103:['Carne Picada','Cat.V','Vacuno',10500,'picada.png'],
    107:['Abastero','Cat.V','Vacuno',9900,'abastero.png'],
    108:['Carnicero','Cat.V','Vacuno',9900,'carnicero.png'],
    101:['Huachalomo','Cat.V','Vacuno',9900,'huachalomo.png'],
    109:['Sobrecostilla','Cat.V','Vacuno',9900,'sobrecostilla.png'],
    116:['Tapapecho','Cat.V','Vacuno',8900,'tapapecho.png'],
}
carnesordeMe = {
    116:['Tapapecho','Cat.V','Vacuno',8900,'tapapecho.png'],
    101:['Huachalomo','Cat.V','Vacuno',9900,'huachalomo.png'],
    104:['Posta Negra','Cat.V','Vacuno',10800,'postaN.png'],
    107:['Abastero','Cat.V','Vacuno',9900,'abastero.png'],
    108:['Carnicero','Cat.V','Vacuno',9900,'carnicero.png'],
    109:['Sobrecostilla','Cat.V','Vacuno',9900,'sobrecostilla.png'],
    103:['Carne Picada','Cat.V','Vacuno',10500,'picada.png'],
    102:['Molida Especial','Cat.V','Vacuno',10500,'molida.png'],
    105:['Posta Rosada','Cat.V','Vacuno',10800,'postaR.png'],
    106:['Posta Paleta','Cat.V','Vacuno',10990,'postaP.png'],
    110:['Punta Paleta','Cat.V','Vacuno',11200,'puntaP.png'],
    115:['Asiento','Cat.V','Vacuno',12500,'asiento.png'],
    117:['Lomo Vetado','Cat.V','Vacuno',12900,'lomovetado.png'],
    113:['Palanca','Cat.V','Vacuno',14500,'palanca.png'],
    114:['Filete','Cat.V','Vacuno',15600,'filete.png'],
    112:['Entraña','Cat.V','Vacuno',15900,'entraña.png'],
    111:['Tapabarriga','Cat.V','Vacuno',15900,'tapabarriga.png'],
}
pavo = {
    127:['Costilla de Pavo','Sopraval','Pavo',4900,'costiPavo.png'],
    128:['truto parrillero de pavo','Sopraval','Pavo',5390,'trutoPavo.png'],
    154:['Osobuco pavo','Sopraval','Pavo',3500,'osobucopavo.png'],
    155:['Pechuga de pavo','Sopraval','Pavo',7390,'pechugapavo.png'],
    156:['Tutro corto con hueso de pavo','Sopraval','Pavo',4900,'trutocortopavo.png'],
}
pavoMa = {
    155:['Pechuga de pavo','Sopraval','Pavo',7390,'pechugapavo.png'],
    128:['truto parrillero de pavo','Sopraval','Pavo',5390,'trutoPavo.png'],
    127:['Costilla de Pavo','Sopraval','Pavo',4900,'costiPavo.png'],
    156:['Tutro corto con hueso de pavo','Sopraval','Pavo',4900,'trutocortopavo.png'],
    154:['Osobuco pavo','Sopraval','Pavo',3500,'osobucopavo.png'],
}
pavoMe= {
    154:['Osobuco pavo','Sopraval','Pavo',3500,'osobucopavo.png'],
    127:['Costilla de Pavo','Sopraval','Pavo',4900,'costiPavo.png'],
    156:['Tutro corto con hueso de pavo','Sopraval','Pavo',4900,'trutocortopavo.png'],
    128:['truto parrillero de pavo','Sopraval','Pavo',5390,'trutoPavo.png'],
    155:['Pechuga de pavo','Sopraval','Pavo',7390,'pechugapavo.png'],
}
aves = {
    118:['Presitas de pollo','Don Pollo','Pollo',4100,'polloP.png'],
    119:['Truto Entero','Don Pollo','Pollo',3290,'trutopollo.png'],
    120:['Pechuga Entera','Don Pollo','Pollo',4290,'polloPechuga.png'],
    # 121:['Pechuga Deshuesada','Don Pollo','Pollo',5500,'pechugadeshue.png'],
    122:['Pata de pollo','Don Pollo','Pollo',2400,'patapollo.png'],
    # 123:['Contre pollo','Don Pollo','Pollo',1200,'contrepollo.png'],
    124:['Higado de pollo','Don Pollo','Pollo',1200,'higadopollo.png'],
    # 125:['Truto ala','Don Pollo','Pollo',4500,'trutoala.png'],
    # 126:['Alas de pollo','Don Pollo','Pollo',3990,'alapollo.png'],
}
avesMa = {
    121:['Pechuga Deshuesada','Don Pollo','Pollo',5500,'pechugadeshue.png'],
    125:['Truto ala','Don Pollo','Pollo',4500,'trutoala.png'],
    120:['Pechuga Entera','Don Pollo','Pollo',4290,'polloPechuga.png'],
    118:['Presitas de pollo','Don Pollo','Pollo',4100,'polloP.png'],
    126:['Alas de pollo','Don Pollo','Pollo',3990,'alapollo.png'],
    119:['Truto Entero','Don Pollo','Pollo',3290,'trutopollo.png'],
    122:['Pata de pollo','Don Pollo','Pollo',2400,'patapollo.png'],
    123:['Contre pollo','Don Pollo','Pollo',1200,'contrepollo.png'],
    124:['Higado de pollo','Don Pollo','Pollo',1200,'higadopollo.png'],
}
avesMe = {
    124:['Higado de pollo','Don Pollo','Pollo',1200,'higadopollo.png'],
    123:['Contre pollo','Don Pollo','Pollo',1200,'contrepollo.png'],
    122:['Pata de pollo','Don Pollo','Pollo',2400,'patapollo.png'],
    119:['Truto Entero','Don Pollo','Pollo',3290,'trutopollo.png'],
    126:['Alas de pollo','Don Pollo','Pollo',3990,'alapollo.png'],
    118:['Presitas de pollo','Don Pollo','Pollo',4100,'polloP.png'],
    120:['Pechuga Entera','Don Pollo','Pollo',4290,'polloPechuga.png'],
    125:['Truto ala','Don Pollo','Pollo',4500,'trutoala.png'],
    121:['Pechuga Deshuesada','Don Pollo','Pollo',5500,'pechugadeshue.png'],
}

cerdo = {
    129:['Costillar de cerdo','AgroSuper','Cerdo',7900,'costillar.png'],
    130:['Pulpa sin hueso','AgroSuper','Cerdo',6300,'pulpasinhueso.png'],
    131:['Pulpa pierna','AgroSuper','Cerdo',5900,'pulpapierna.png'],
    132:['Paleta de cerdo','AgroSuper','Cerdo',5800,'paletacerdo.png'],
    133:['Chuleta centro','AgroSuper','Cerdo',6190,'chuletacentro.png'],
    134:['Chuleta vetada','AgroSuper','Cerdo',6190,'chuletavetada.png'],
    135:['Lomo de cerdo ','AgroSuper','Cerdo',6500,'lomocerdo.png'],
    
}
cerdoMa = {
    129:['Costillar de cerdo','AgroSuper','Cerdo',7900,'costillar.png'],
    135:['Lomo de cerdo ','AgroSuper','Cerdo',6500,'lomocerdo.png'],
    130:['Pulpa sin hueso','AgroSuper','Cerdo',6300,'pulpasinhueso.png'],
    134:['Chuleta vetada','AgroSuper','Cerdo',6190,'chuletavetada.png'],
    133:['Chuleta centro','AgroSuper','Cerdo',6190,'chuletacentro.png'],
    131:['Pulpa pierna','AgroSuper','Cerdo',5900,'pulpapierna.png'],
    132:['Paleta de cerdo','AgroSuper','Cerdo',5800,'paletacerdo.png'],
    
}
cerdoMe = {
    132:['Paleta de cerdo','AgroSuper','Cerdo',5800,'paletacerdo.png'],
    131:['Pulpa pierna','AgroSuper','Cerdo',5900,'pulpapierna.png'],
    133:['Chuleta centro','AgroSuper','Cerdo',6190,'chuletacentro.png'],
    134:['Chuleta vetada','AgroSuper','Cerdo',6190,'chuletavetada.png'],
    130:['Pulpa sin hueso','AgroSuper','Cerdo',6300,'pulpasinhueso.png'],
    135:['Lomo de cerdo ','AgroSuper','Cerdo',6500,'lomocerdo.png'],
    129:['Costillar de cerdo','AgroSuper','Cerdo',7900,'costillar.png'],
    
}

cazuela = {
    136:['Hueso carnudo','Cat.V','Vacuno',5400,'huesocarnudo.png'],
    139:['Osobuco','Cat.V','Vacuno',8100,'osobuco.png'],
    137:['Aletilla','Cat.V','Vacuno',6900,'aletilla.png'],
    138:['Coluda','Cat.V','Vacuno',6900,'coluda.png'],
    140:['Asado tira','Cat.V','Vacuno',11500,'asadotira.png'],
    
}
cazuelaMa = {
    140:['Asado tira','Cat.V','Vacuno',11500,'asadotira.png'],
    139:['Osobuco','Cat.V','Vacuno',8100,'osobuco.png'],
    137:['Aletilla','Cat.V','Vacuno',6900,'aletilla.png'],
    138:['Coluda','Cat.V','Vacuno',6900,'coluda.png'],
    136:['Hueso carnudo','Cat.V','Vacuno',5400,'huesocarnudo.png'],
    
}
cazuelaMe = {
    136:['Hueso carnudo','Cat.V','Vacuno',5400,'huesocarnudo.png'],
    137:['Aletilla','Cat.V','Vacuno',6900,'aletilla.png'],
    138:['Coluda','Cat.V','Vacuno',6900,'coluda.png'],
    139:['Osobuco','Cat.V','Vacuno',8100,'osobuco.png'],
    140:['Asado tira','Cat.V','Vacuno',11500,'asadotira.png'],
    
}

interiores = {
    141:['Higado de vacuno','Cat.V','Vacuno',4900,'higadov.png'],
    142:['Corazon','Cat.V','Vacuno',4900,'corazon.png'],
    143:['Pata de vacuno','Cat.V','Vacuno',3500,'patav.png'],
    144:['Guata cayo','Cat.V','Vacuno',5900,'guatac.png'],
    145:['Guata Surtida','Cat.V','Vacuno',4900,'guatas.png'],
    146:['Chunchule','Cat.V','Vacuno',5900,'chunchule.png'],
}
interioresMa = {
    144:['Guata cayo','Cat.V','Vacuno',5900,'guatac.png'],
    146:['Chunchule','Cat.V','Vacuno',5900,'chunchule.png'],
    141:['Higado de vacuno','Cat.V','Vacuno',4900,'higadov.png'],
    142:['Corazon','Cat.V','Vacuno',4900,'corazon.png'],
    145:['Guata Surtida','Cat.V','Vacuno',4900,'guatas.png'],
    143:['Pata de vacuno','Cat.V','Vacuno',3500,'patav.png'],
}
interioresMe = {
    143:['Pata de vacuno','Cat.V','Vacuno',3500,'patav.png'],
    141:['Higado de vacuno','Cat.V','Vacuno',4900,'higadov.png'],
    142:['Corazon Vacuno','Cat.V','Vacuno',4900,'corazon.png'],
    145:['Guata Surtida','Cat.V','Vacuno',4900,'guatas.png'],
    144:['Guata cayo','Cat.V','Vacuno',5900,'guatac.png'],
    146:['Chunchule','Cat.V','Vacuno',5900,'chunchule.png'],
}

embutidos = {
    147:['Longaniza de chillan','Cecinas ñuble','Embutido',8500,'longaniza.png'],
    148:['Vianessa Tradicional','San Jorge','Embutido',2300,'vianessaT.png'],
    149:['Vianessa Sureña','San Jorge','Embutido',2400,'vianessaS.png'],
    150:['Vianessa Pollo','San Jorge','Embutido',2100,'vianessaP.png'],
    151:['Chorizo','La preferida','Embutido',2800,'chorizo.png'],
    152:['Chorisillo','Receta del abuelo','Embutido',3100,'chorisillo.png'],
}
embutidosordeM = {
    147:['Longaniza de chillan','Cecinas ñuble','Embutido',8500,'longaniza.png'],
    152:['Chorisillo','Receta del abuelo','Embutido',3100,'chorisillo.png'],
    151:['Chorizo','La preferida','Embutido',2800,'chorizo.png'],
    148:['Vianessa Tradicional','San Jorge','Embutido',2300,'vianessaT.png'],
    149:['Vianessa Sureña','San Jorge','Embutido',2400,'vianessaS.png'],
    150:['Vianessa Pollo','San Jorge','Embutido',2100,'vianessaP.png'],
}
embutidosordeMe = {
    150:['Vianessa Pollo','San Jorge','Embutido',2100,'vianessaP.png'],
    148:['Vianessa Tradicional','San Jorge','Embutido',2300,'vianessaT.png'],
    149:['Vianessa Sureña','San Jorge','Embutido',2400,'vianessaS.png'],
    151:['Chorizo','La preferida','Embutido',2800,'chorizo.png'],
    152:['Chorisillo','Receta del abuelo','Embutido',3100,'chorisillo.png'],
    153:['Longaniza de chillan','Cecinas ñuble','Embutido',8500,'longaniza.png'],
}

ventas = [
    {
        "nombre_producto": "Carne de vacuno",
        "kilos": 2,
        "precio": 4000,
        "imagen": "https://agrocomercial.cl/wp-content/uploads/2022/06/Carne-picada-vacuno-e1665727483313.jpg",
    },
    {
        "nombre_producto": "Trutro de pollo",
        "kilos": 3,
        "precio": 6800,
        "imagen": "https://santaisabel.vtexassets.com/arquivos/ids/168471/Trutro-entero-de-pollo-granel.jpg?v=637503135889930000",
    },
    {
        "nombre_producto": "Pechuga de pollo deshuesada",
        "kilos": 2,
        "precio": 7500,
        "imagen": "https://santaisabel.vtexassets.com/arquivos/ids/168471/Trutro-entero-de-pollo-granel.jpg?v=637503135889930000",
    },
]

carnes1 = {
    "descripción1":['Lomovetado','lomovetado.jpeg',1],
    "descripción2":['PostaPaleta','postapaleta.jpeg',3],
    "descripción3":['CarneCerdo','carneCerdo.jpg',5],
    "descripción4":['CarneVacuno','carnevacuno.jpeg',2],
    "descripción5":['Pollo','pollo.jpg',1],
    "descripción6":['PolloGanso','polloganso.jpeg',2],
}
carnes2 = {
    "descripción4":['CarneVacuno','carnevacuno.jpeg',2],
    "descripción3":['CarneCerdo','carneCerdo.jpg',1],
    "descripción2":['PostaPaleta','postapaleta.jpeg',3],
    "descripción1":['lomovetado','lomovetado.jpeg',4],
    "descripción5":['Pollo','pollo.jpg',1],
    "descripción6":['PolloGanso','polloganso.jpeg',2],
}
cliente = [
    {'nombre':'Pedro','nroOrden1':'2313','nroOrden2':'1512','cantidad':'4'}
]

carne = {
    "descripción6":['polloganso','polloganso.jpeg',2],
    "descripción3":['carneCerdo','carneCerdo.jpg',4],
    "descripción1":['lomovetado','lomovetado.jpeg',1],
}
cliente1 = [
    {'nombre':'Pedro','nroOrden':'2','cantidad':'4'}
]

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
    creado = models.DateTimeField(default=timezone.now)

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