# LibreDrop — Backend

API REST de LibreDrop construida con Django 6 y Django REST Framework.

## Stack

- Python 3.12+
- Django 6
- Django REST Framework 3.17
- Autenticación JWT (djangorestframework-simplejwt)
- Cloudinary (imágenes)
- PostgreSQL (producción) / SQLite (desarrollo)
- python-dotenv

## Requisitos

- Python 3.12+
- pip

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edita `.env` con tus credenciales (al menos `SECRET_KEY` y las de Cloudinary si usas imágenes).

Para desarrollo con SQLite, agrega a tu `.env`:

```
DB_ENGINE=django.db.backends.sqlite3
```

```bash
python manage.py migrate
python manage.py runserver
```

## Estructura

```
backend/
├── accounts/      # Usuarios: registro, login y gestión
├── catalog/       # Categorías y productos
├── shop/          # Tiendas
├── libredrop/     # Configuración del proyecto (settings, urls)
├── manage.py
├── requirements.txt
└── .env.example
```

## Apps

| App | Descripción |
|-----|-------------|
| `accounts` | Registro, inicio de sesión y gestión de usuarios |
| `shop` | Creación y configuración de tiendas |
| `catalog` | Gestión de categorías y productos |

## Modelos

| Modelo | App | Descripción |
|--------|-----|-------------|
| `User` | accounts | Usuario (AbstractUser) con `payment_verified`, `created_at`, `updated_at` |
| `Shop` | shop | Tienda con dueño, slug único, WhatsApp, logo |
| `Category` | catalog | Categoría de una tienda (slug único por tienda) |
| `Product` | catalog | Producto de una tienda, categoría opcional |

Relaciones principales:

- `User` 1→N `Shop` (`Shop.owner`)
- `Shop` 1→N `Category` (`Category.shop`)
- `Shop` 1→N `Product` (`Product.shop`)
- `Category` 1→N `Product` (`Product.category`, opcional, `SET_NULL`)

Ver [docs/ARCHITECTURE.md](../docs/ARCHITECTURE.md) para el detalle completo.

## Autenticación

La API usa JWT mediante `djangorestframework-simplejwt`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
```

Para obtener un token de acceso envías las credenciales del usuario y recibes un `access` y un `refresh` token. El token de acceso se envía como `Authorization: Bearer <access>`.

## Variables de entorno

| Variable | Descripción | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Clave secreta de Django | `django-insecure-default-dev-key` |
| `DEBUG` | Modo depuración | `False` |
| `ALLOWED_HOSTS` | Hosts permitidos (coma separados) | vacío |
| `CLOUDINARY_CLOUD_NAME` | Cloud name de Cloudinary | vacío |
| `CLOUDINARY_API_KEY` | API key de Cloudinary | vacío |
| `CLOUDINARY_API_SECRET` | API secret de Cloudinary | vacío |
| `DB_ENGINE` | Motor de base de datos | `django.db.backends.postgresql` |
| `DB_NAME` | Nombre de la base de datos | `db.sqlite3` |
| `DB_USER` | Usuario de la base de datos | vacío |
| `DB_PASSWORD` | Contraseña de la base de datos | vacío |
| `DB_HOST` | Host de la base de datos | vacío |
| `DB_PORT` | Puerto de la base de datos | vacío |

## Comandos útiles

```bash
python manage.py migrate                 # Aplicar migraciones
python manage.py makemigrations          # Crear migraciones
python manage.py createsuperuser         # Crear usuario admin
python manage.py runserver               # Servidor de desarrollo
python manage.py test                    # Ejecutar tests
```

## Documentación relacionada

- [docs/API.md](../docs/API.md) — referencia de la API REST.
- [docs/DEPLOYMENT.md](../docs/DEPLOYMENT.md) — guía de despliegue.
