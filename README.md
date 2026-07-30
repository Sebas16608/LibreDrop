# LibreDrop

**LibreDrop** es una plataforma open source para crear tiendas online simples. Hecha en Guatemala bajo licencia AGPLv3.

- Crea tu tienda, publica productos y recibe pedidos por WhatsApp.
- Sin intermediarios ni comisiones. Tú controlas tus datos y API keys.
- Arquitectura modular con Django y Django REST Framework.

## Stack

| Capa | Tecnología |
|------|-----------|
| Backend | Python 3.12+, Django 6, DRF |
| Base de datos | PostgreSQL (producción) / SQLite (desarrollo) |
| Imágenes | Cloudinary |
| API | REST |

## Requisitos

- Python 3.12+
- pip

## Instalación

```bash
# Clonar el repositorio
git clone git@github.com:Sebas16608/LibreDrop.git
cd LibreDrop/backend

# Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Edita .env con tus credenciales

# Migrar base de datos
python manage.py migrate

# Iniciar servidor de desarrollo
python manage.py runserver
```

## Configuración

Copia `.env.example` a `.env` y completa las variables:

| Variable | Descripción |
|----------|-------------|
| `SECRET_KEY` | Clave secreta de Django |
| `DEBUG` | True para desarrollo |
| `ALLOWED_HOSTS` | Hosts permitidos |
| `CLOUDINARY_CLOUD_NAME` | Tu cloud name de Cloudinary |
| `CLOUDINARY_API_KEY` | Tu API key de Cloudinary |
| `CLOUDINARY_API_SECRET` | Tu API secret de Cloudinary |
| `DB_ENGINE` | Motor de BD (opcional, default SQLite) |
| `DB_NAME`, `DB_USER`, etc. | Credenciales de PostgreSQL (opcional) |

## Apps

| App | Descripción |
|-----|-------------|
| `accounts` | Registro, inicio de sesión y gestión de usuarios |
| `shop` | Creación y configuración de tiendas |
| `catalog` | Gestión de categorías y productos |

## Documentación

- [VERSIONS.md](docs/VERSIONS.md) — versionado y características del proyecto.
- [CONTRIB.md](CONTRIB.md) — guía para contribuir.
- [Backend README](backend/README.md) — documentación técnica del backend.

## Licencia

AGPLv3 — ver [LICENSE](LICENSE).
