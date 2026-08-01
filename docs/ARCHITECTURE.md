# Arquitectura de LibreDrop

## Visión general

LibreDrop es una aplicación **multi-tenant** construida con Django. El proyecto se organiza en apps de Django con responsabilidades separadas:

```
┌─────────────────────────────────────────────┐
│                  Frontend                    │
│  Landing pages estáticas (HTML/CSS/JS)       │
│  Página pública de la tienda (futuro)        │
└──────────────────┬──────────────────────────┘
                   │  HTTPS / REST
┌──────────────────▼──────────────────────────┐
│                 API REST                     │
│       Django + Django REST Framework         │
│  Autenticación: JWT (simplejwt)              │
├─────────────────────────────────────────────┤
│   accounts        │   shop       │  catalog  │
│  (usuarios)       │  (tiendas)   │(cat/prod) │
└──────────────────┬──────────────────────────┘
                   │
          ┌────────▼────────┐     ┌────────────┐
          │  Base de datos   │     │ Cloudinary │
          │  PostgreSQL/SQLite│    │ (imágenes) │
          └─────────────────┘     └────────────┘
```

## Apps

### accounts

Gestión de usuarios. Define el modelo `User` personalizado como `AUTH_USER_MODEL`, derivado de `AbstractUser`.

| Campo | Tipo | Notas |
|-------|------|-------|
| `username` | CharField | Heredado de Django |
| `email` | EmailField | Heredado de Django |
| `payment_verified` | BooleanField | Indica si el pago fue verificado (default `False`) |
| `created_at` | DateTimeField | Auto al crear |
| `updated_at` | DateTimeField | Auto al actualizar |

Usado para el registro de usuarios con generación de tokens JWT.

### shop

Representa las tiendas. Una tienda pertenece a un único dueño (`owner`).

| Campo | Tipo | Notas |
|-------|------|-------|
| `owner` | FK → `User` | `on_delete=CASCADE`, `related_name="shops"` |
| `name` | CharField(255) | Nombre de la tienda |
| `slug` | SlugField | Único a nivel global |
| `description` | TextField | Opcional |
| `logo` | CloudinaryField | Imagen, opcional |
| `whatsapp_number` | CharField(20) | Número para recibir pedidos |
| `is_active` | BooleanField | Default `True` |
| `created_at` / `updated_at` | DateTimeField | Timestamps |

### catalog

Categorías y productos del catálogo de cada tienda.

**Category**

| Campo | Tipo | Notas |
|-------|------|-------|
| `shop` | FK → `Shop` | `on_delete=CASCADE`, `related_name="categories"` |
| `name` | CharField(255) | Nombre |
| `slug` | SlugField | Único por tienda (`unique_together`) |
| `description` | TextField | Opcional |
| `created_at` / `updated_at` | DateTimeField | Timestamps |

**Product**

| Campo | Tipo | Notas |
|-------|------|-------|
| `shop` | FK → `Shop` | `on_delete=CASCADE`, `related_name="products"` |
| `category` | FK → `Category` | `on_delete=SET_NULL`, `null=True`, `blank=True` |
| `name` | CharField(255) | Nombre |
| `slug` | SlugField | Único por tienda (`unique_together`) |
| `description` | TextField | Opcional |
| `price` | DecimalField(10,2) | Precio de venta |
| `purchase_price` | DecimalField(10,2) | Precio de compra interno, opcional |
| `discount` | DecimalField(5,2) | Descuento, default `0` |
| `stock` | PositiveIntegerField | Default `0` |
| `image` | CloudinaryField | Imagen, opcional |
| `is_active` | BooleanField | Default `True` |
| `created_at` / `updated_at` | DateTimeField | Timestamps |

## Diagrama de relaciones

```
User ───< Shop ───< Category
                  └──< Product ───< (opcional) Category
```

- `User` 1→N `Shop` (via `Shop.owner`)
- `Shop` 1→N `Category` (via `Category.shop`)
- `Shop` 1→N `Product` (via `Product.shop`)
- `Category` 1→N `Product` (via `Product.category`, opcional)

## Multi-tenant

Cada `Shop` aísla sus `Category` y `Product`. La unicidad de slugs de categorías y productos se define **por tienda** (`unique_together = ("shop", "slug")`), de modo que dos tiendas distintas pueden usar el mismo slug sin colisionar.

Todo acceso a datos del catálogo debe filtrarse por `shop` para evitar fugas entre tiendas.

## Flujo de compra (v1.0)

1. El cliente visita la página pública de la tienda.
2. Ve los productos activos.
3. Pulsa **"Comprar por WhatsApp"**.
4. El sistema genera un enlace a WhatsApp con la información del producto.
5. La compra se negocia directamente por WhatsApp con el dueño.

No existe carrito, pasarela de pago ni órdenes internas en v1.0.

## Configuración relevante

- `AUTH_USER_MODEL = "accounts.User"` — modelo de usuario personalizado.
- `REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']` — autenticación JWT por defecto.
- `CLOUDINARY_STORAGE` — credenciales de Cloudinary para almacenamiento de imágenes.
- `django_cleanup` — elimina imágenes del storage al borrar modelos.

## Documentación relacionada

- [VERSIONS.md](VERSIONS.md) — características por versión.
- [API.md](API.md) — referencia de la API REST.
