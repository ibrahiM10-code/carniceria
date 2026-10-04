# Carnicería

Aplicación web para una carnicería, desarrollada con Django. Incluye un catálogo de productos por categoría, carrito y flujo de compra, gestión de categorías/productos y cajeros, y una API REST para categorías.

## Tecnologías

- Python y Django
- MySQL (`mysqlclient`)
- Django REST Framework
- PayPal Sandbox para el flujo de pago
- Plantillas HTML, CSS y archivos estáticos del proyecto

Las dependencias de Python están listadas en [`dependencies.txt`](./dependencies.txt).

## Requisitos

- Python instalado
- MySQL Server en ejecución
- Credenciales de una base de datos MySQL local
- Credenciales de PayPal Sandbox para probar pagos

## Instalación y configuración

1. Clona el repositorio y entra a la carpeta del proyecto.

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <CARPETA_DEL_PROYECTO>
   ```

2. Crea y activa un entorno virtual.

   En Windows PowerShell:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   En macOS o Linux:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   python -m pip install -r dependencies.txt
   ```

4. Crea una base de datos MySQL vacía. La configuración actual conecta a `localhost:3306`.

5. Crea un archivo `.env` en la raíz del proyecto y completa las variables requeridas:

   ```dotenv
   NAME=nombre_de_la_base
   USER=usuario_mysql
   PASSWORD=clave_mysql
   CLIENT_ID=id_de_aplicacion_paypal_sandbox
   CLIENT_SECRET=secreto_de_aplicacion_paypal_sandbox
   API_SANDBOX=https://api-m.sandbox.paypal.com
   PORT=http://127.0.0.1:8000/
   DESDE_EMAIL=correo_para_envios
   PSW_EMAIL=clave_o_credencial_de_aplicacion
   ```

   `.env` contiene secretos: no lo publiques ni lo agregues al control de versiones. Usa credenciales de prueba de PayPal Sandbox; configura correo y pago solo si vas a probar esas funciones.

6. Aplica las migraciones:

   ```bash
   python manage.py migrate
   ```

   El archivo [`Script BD.sql`](./Script%20BD.sql) contiene una exportación SQL de la base de datos. Úsala solo si necesitas restaurar esa exportación en lugar de inicializar la base mediante migraciones; evita importar el volcado sobre una base ya preparada con `migrate`.

7. (Opcional) Crea un usuario administrador:

   ```bash
   python manage.py createsuperuser
   ```

## Ejecutar en desarrollo

```bash
python manage.py runserver
```

Abre <http://127.0.0.1:8000/> en el navegador. El panel estándar de Django está en <http://127.0.0.1:8000/admin/>.

## Rutas principales

| Ruta | Descripción |
| --- | --- |
| `/` | Inicio y catálogo de la tienda |
| `/carnes/`, `/embutidos/`, `/aves/`, `/cerdo/`, `/interiores/`, `/cazuela/`, `/pavo/` | Categorías de productos |
| `/miCarrito/` | Carrito de compras |
| `/registrarse/`, `/login_user/`, `/logout_user` | Registro e inicio/cierre de sesión |
| `/recuperarClave/` | Flujo de recuperación de contraseña |
| `/panel-admin/menu/` | Menú de administración de la aplicación |
| `/categoriasRest/` | API de categorías |
| `/categoriasRest/<id>/` | Operaciones sobre una categoría específica |

La API de categorías acepta `GET` y `POST` en `/categoriasRest/`, y `GET`, `PUT` y `DELETE` en `/categoriasRest/<id>/`.

## Estructura del proyecto

```text
carni/          Configuración general de Django y rutas raíz
app1/           Tienda, catálogo, cuentas, carrito y compras
carniCruds/     Vistas de administración para categorías, productos y cajeros
carniRest/      Serializador y endpoints REST de categorías
templates/      Plantillas HTML
static/         Archivos estáticos
media/          Imágenes y otros archivos subidos
Script BD.sql   Exportación SQL de la base de datos
```

## Notas

- La configuración incluida está orientada al desarrollo local. Antes de desplegar, configura de forma segura `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, base de datos y credenciales, y revisa la lista de verificación de despliegue de Django.
- No se incluyen pruebas automatizadas documentadas en el proyecto. Puedes comprobar que el proyecto carga con `python manage.py check`.
