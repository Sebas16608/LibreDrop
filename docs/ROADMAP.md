# Hoja de ruta de LibreDrop

## Visión

LibreDrop busca ser la plataforma open source de referencia para crear tiendas online simples, sin intermediarios ni comisiones, manteniendo la soberanía de los datos del usuario. Hecho en Guatemala bajo AGPLv3.

## v1.0 — MVP (en desarrollo)

Objetivo: validar la idea y conseguir los primeros usuarios.

### Backend

- [x] Modelo de usuario personalizado (`accounts.User`).
- [x] Modelos de `Shop`, `Category` y `Product`.
- [x] Multi-tenant por tienda (slugs únicos por tienda).
- [x] Configuración JWT (simplejwt).
- [x] Serializer de registro con tokens.
- [ ] Vistas y URLs de registro/login.
- [ ] CRUD de tiendas.
- [ ] CRUD de categorías y productos.
- [ ] Endpoint público de la tienda.
- [ ] Enlace "Comprar por WhatsApp" por producto.

### Frontend

- [x] Landing de LibreDrop.
- [x] Landing de LibreDrop Cloud.
- [ ] Panel de administración de la tienda.
- [ ] Página pública de la tienda (frontend).

## v1.1 / v1.2 — Consolidación

- [ ] Tests automatizados para los modelos y la API.
- [ ] Documentación de la API con drf-spectacular (OpenAPI/Swagger).
- [ ] Paginación y filtros en listados.
- [ ] Roles y permisos más finos (colaboradores de tienda).

## v2.0 — Comercio

- [ ] Carrito de compras.
- [ ] Gestión de órdenes internas.
- [ ] Métodos de pago.
- [ ] Notificaciones por correo.
- [ ] Estadísticas de ventas.

## v2.1+ — Escalado

- [ ] Integraciones con empresas de envío.
- [ ] Planes de suscripción.
- [ ] Personalización avanzada de tiendas.
- [ ] Marketplace / temas.

## Prioridades de la comunidad

La hoja de ruta se ajusta según la retroalimentación de la comunidad y los early adopters. Si tienes una propuesta, abre un issue en [GitHub Issues](https://github.com/Sebas16608/LibreDrop/issues).

## Documentación relacionada

- [VERSIONS.md](VERSIONS.md) — detalle de las características de v1.0.
