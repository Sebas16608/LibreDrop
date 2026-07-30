# LibreDrop v1.0

## Objetivo

LibreDrop es una plataforma open source para crear tiendas online simples. La versión v1.0 (MVP) está diseñada para que emprendedores puedan crear una tienda, publicar sus productos y recibir pedidos mediante WhatsApp, eliminando la necesidad de infraestructura compleja o pasarelas de pago desde el inicio.

## Características incluidas

### Accounts

- Registro de usuarios.
- Inicio de sesión.
- Gestión básica de usuarios.

### Shops

- Creación de tiendas.
- Cada usuario puede tener una tienda.
- Nombre de tienda.
- Slug único.
- Descripción.
- Logo.
- Número de WhatsApp.
- Página pública de la tienda.

### Catalog

- Creación de categorías.
- Creación de productos.
- Productos asociados a una tienda.
- Productos asociados opcionalmente a categorías.
- Nombre del producto.
- Descripción.
- Precio.
- Precio de compra interno.
- Descuento.
- Stock.
- Imagen del producto.
- Estado activo/inactivo.

### Compras

- No existe carrito.
- No existen pagos integrados.
- No existen órdenes internas.
- El cliente compra mediante un botón "Comprar por WhatsApp".
- El sistema genera un enlace de WhatsApp con la información del producto.

## Arquitectura inicial

LibreDrop utiliza una arquitectura modular basada en Django apps:

- **accounts** — gestión de usuarios, registro e inicio de sesión.
- **shop** — creación y configuración de tiendas.
- **catalog** — gestión de categorías y productos.

Cada módulo tiene responsabilidades separadas y puede desarrollarse de forma independiente.

## Multi-tenant

LibreDrop está diseñado como una aplicación multi-tenant donde cada tienda tiene sus propios productos y categorías aisladas. Los datos de cada tienda no son accesibles desde otras tiendas, garantizando la privacidad y seguridad de la información.

## Funcionalidades fuera de v1.0

- Carrito de compras.
- Gestión de órdenes.
- Métodos de pago.
- Integraciones con empresas de envío.
- Notificaciones por correo.
- Estadísticas de ventas.
- Planes de suscripción.
- Personalización avanzada de tiendas.

## Estado del proyecto

v1.0 es una versión MVP enfocada en validar la idea y conseguir los primeros usuarios. Las funcionalidades listadas como fuera de v1.0 están planificadas para versiones futuras basadas en la retroalimentación de la comunidad y los early adopters.
