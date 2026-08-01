# API REST de LibreDrop

Referencia de la API REST de LibreDrop. Base URL local: `http://127.0.0.1:8000/`.

## Autenticación

Toda la API usa tokens JWT (`djangorestframework-simplejwt`). Los endpoints protegidos requieren el header:

```
Authorization: Bearer <access_token>
```

Los tokens se obtienen en el registro de usuario y (futuro) en el login.

### Endpoints de JWT (simplejwt)

| Método | Ruta | Descripción |
|--------|------|-------------|
| `POST` | `/api/token/` | Obtener `access` y `refresh` tokens |
| `POST` | `/api/token/refresh/` | Renovar el token de acceso |
| `POST` | `/api/token/verify/` | Verificar que un token es válido |

## Registro de usuario

### `POST /api/auth/register/`

Crea un usuario y devuelve los tokens de acceso.

**Implementación:** el serializer `RegisterSerializer` está listo en `backend/accounts/serializers.py`. La vista aún no está conectada a las URLs.

**Cuerpo de la petición:**

```json
{
  "username": "juan",
  "email": "juan@example.com",
  "password": "contraseña_segura",
  "password_confirm": "contraseña_segura"
}
```

**Campos del serializer:**

| Campo | Tipo | Requerido | Notas |
|-------|------|-----------|-------|
| `id` | int | — | Solo lectura (generado) |
| `username` | str | sí | Nombre de usuario |
| `email` | str | sí | No puede ir vacío |
| `password` | str | sí | Solo escritura |
| `password_confirm` | str | sí | Solo escritura, debe coincidir con `password` |
| `is_active` | bool | — | Solo lectura |
| `payment_verified` | bool | — | Solo lectura |

**Respuesta `200 OK`:**

```json
{
  "id": 1,
  "username": "juan",
  "email": "juan@example.com",
  "is_active": true,
  "payment_verified": false,
  "tokens": {
    "refres": "<refresh_token>",
    "access": "<access_token>"
  }
}
```

**Errores posibles:**

- `400 Bad Request` — si las contraseñas no coinciden (`{"password": ["Las contraseñas no coinciden"]}`) o faltan campos requeridos.

## Tiendas y catálogo (planificado)

Los siguientes endpoints están planificados para v1.0 y aún no están implementados:

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` / `POST` | `/api/shops/` | Listar / crear tiendas del usuario autenticado |
| `GET` / `PUT` / `PATCH` / `DELETE` | `/api/shops/{id}/` | Detalle / editar / eliminar una tienda |
| `GET` / `POST` | `/api/shops/{shop_id}/categories/` | Listar / crear categorías de una tienda |
| `GET` / `POST` | `/api/shops/{shop_id}/products/` | Listar / crear productos de una tienda |
| `GET` | `/api/shops/{slug}/` | Página pública de la tienda (sin autenticación) |

## Formato de errores

La API usa los formatos estándar de Django REST Framework:

```json
{
  "campo": ["mensaje de error"]
}
```

## Convenciones

- Respuestas en JSON.
- Rutas de recursos en plural.
- Filtros por `shop` siempre obligatorios para datos del catálogo (multi-tenant).

## Documentación relacionada

- [ARCHITECTURE.md](ARCHITECTURE.md) — modelos y relaciones.
- [VERSIONS.md](VERSIONS.md) — alcance de cada versión.
