# LibreDrop — Backend

API REST de LibreDrop construida con Django 6 y Django REST Framework.

## Stack

- Python 3.12+
- Django 6
- Django REST Framework
- Cloudinary (imágenes)
- PostgreSQL / SQLite (desarrollo)
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

```bash
python manage.py migrate
python manage.py runserver
```

## Apps

| App | Descripción |
|-----|-------------|
| `accounts` | Registro, inicio de sesión y gestión de usuarios |
| `shop` | Creación y configuración de tiendas |
| `catalog` | Gestión de categorías y productos |

## Modelos

Ver `docs/VERSIONS.md` para el detalle de cada modelo y sus relaciones.
