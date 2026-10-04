# Carnicería

A web application for a butcher shop, built with Django. It includes a product catalog organized by category, a shopping cart and checkout flow, category/product and cashier management, and a REST API for categories.

## Technologies

- Python and Django
- MySQL (`mysqlclient`)
- Django REST Framework
- PayPal Sandbox for the payment flow
- HTML templates, CSS, and project static files

Python dependencies are listed in [`dependencies.txt`](./dependencies.txt).

## Requirements

- Python
- A running MySQL Server
- Credentials for a local MySQL database
- PayPal Sandbox credentials to test payments

## Installation and configuration

1. Clone the repository and navigate to the project directory.

   ```bash
   git clone <REPOSITORY_URL>
   cd <PROJECT_DIRECTORY>
   ```

2. Create and activate a virtual environment.

   On Windows PowerShell:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS or Linux:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r dependencies.txt
   ```

4. Create an empty MySQL database. The current configuration connects to `localhost:3306`.

5. Create a `.env` file in the project root and set the required variables:

   ```dotenv
   NAME=database_name
   USER=mysql_user
   PASSWORD=mysql_password
   CLIENT_ID=paypal_sandbox_app_id
   CLIENT_SECRET=paypal_sandbox_app_secret
   API_SANDBOX=https://api-m.sandbox.paypal.com
   PORT=http://127.0.0.1:8000/
   DESDE_EMAIL=email_sender_address
   PSW_EMAIL=email_app_password_or_credential
   ```

   `.env` contains secrets: do not publish it or add it to version control. Use PayPal Sandbox test credentials; configure email and payment credentials only if you intend to test those features.

6. Apply the database migrations:

   ```bash
   python manage.py migrate
   ```

   [`Script BD.sql`](./Script%20BD.sql) contains a SQL database export. Use it only if you need to restore that export instead of initializing the database with migrations; do not import the dump into a database that has already been prepared with `migrate`.

7. (Optional) Create an administrator account:

   ```bash
   python manage.py createsuperuser
   ```

## Run in development

```bash
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser. Django's built-in admin site is available at <http://127.0.0.1:8000/admin/>.

## Main routes

| Route | Description |
| --- | --- |
| `/` | Store home page and product catalog |
| `/carnes/`, `/embutidos/`, `/aves/`, `/cerdo/`, `/interiores/`, `/cazuela/`, `/pavo/` | Product categories |
| `/miCarrito/` | Shopping cart |
| `/registrarse/`, `/login_user/`, `/logout_user` | Registration, sign-in, and sign-out |
| `/recuperarClave/` | Password recovery flow |
| `/panel-admin/menu/` | Application administration menu |
| `/categoriasRest/` | Categories API |
| `/categoriasRest/<id>/` | Operations on a specific category |

The categories API accepts `GET` and `POST` at `/categoriasRest/`, and `GET`, `PUT`, and `DELETE` at `/categoriasRest/<id>/`.

## Project structure

```text
carni/          Django project configuration and root URL routes
app1/           Store, catalog, accounts, cart, and purchases
carniCruds/     Admin views for categories, products, and cashiers
carniRest/      Category REST endpoints and serializer
templates/      HTML templates
static/         Static files
media/          Uploaded images and other files
Script BD.sql   SQL database export
```

## Notes

- The included configuration is intended for local development. Before deployment, securely configure `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, database settings, and credentials, and review Django's deployment checklist.
- No automated tests are documented in the project. You can check that the project loads with `python manage.py check`.
