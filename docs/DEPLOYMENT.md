# Despliegue de LibreDrop

Guía de despliegue del backend (Django) y de las landing pages estáticas.

## Landing pages

Las landing pages son sitios estáticos (HTML/CSS/JS vanilla) y se despliegan de forma independiente en Vercel:

| Landing | Carpeta | Dominio |
|---------|---------|---------|
| LibreDrop | `landing/libredrop/` | `https://libredrop.vercel.app` |
| LibreDrop Cloud | `landing/libredrop_cloud/` | `https://libredrop-cloud.vercel.app` |

### Despliegue en Vercel

1. Empuja la carpeta de la landing a un repositorio de Git (o usa Vercel CLI).
2. En Vercel crea un proyecto y selecciona como **Root Directory** la carpeta de la landing (`landing/libredrop` o `landing/libredrop_cloud`).
3. Framework: **Other**. No hay build command (sitio estático puro).
4. Despliega. Cada landing tiene sus propios assets locales (`assets/`), por lo que no dependen entre sí.

> Los metadatos `og:image` y los enlaces entre landings usan URLs absolutas
> (`https://libredrop.vercel.app/...` y `https://libredrop-cloud.vercel.app/...`).
> Si despliegas en otro dominio, actualiza esos valores en el `<head>` de cada `index.html`.

## Backend (Django)

### Variables de entorno

Copia `.env.example` a `.env` y ajusta:

- `SECRET_KEY` — usa una clave segura (genera una con `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`).
- `DEBUG=False`.
- `ALLOWED_HOSTS` — el dominio de tu API, separado por comas.
- Credenciales de Cloudinary si usas imágenes.
- Datos de PostgreSQL.

### Base de datos

En producción usa PostgreSQL:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=libredrop
DB_USER=libredrop
DB_PASSWORD=tu_password_segura
DB_HOST=localhost
DB_PORT=5432
```

### Opción A — VPS (Docker o Gunicorn + Nginx)

Con Gunicorn + Nginx:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

# Servir la API
gunicorn libredrop.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

Configura Nginx como proxy reverso:

```nginx
server {
    listen 80;
    server_name api.example.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Opción B — PaaS (Railway, Render, Fly.io, etc.)

1. Sube el repositorio a la plataforma.
2. Define **Root Directory**: `backend`.
3. Comando de build: `pip install -r requirements.txt`.
4. Comando de start: `gunicorn libredrop.wsgi:application`.
5. Define todas las variables de entorno en el panel de la plataforma.
6. Ejecuta `python manage.py migrate` (como step de release o manualmente).

## Documentación relacionada

- [ARCHITECTURE.md](ARCHITECTURE.md) — arquitectura del proyecto.
- [API.md](API.md) — referencia de la API REST.
- [landing/README.md](../landing/README.md) — detalle de las landing pages.
