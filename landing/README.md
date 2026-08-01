# Landing pages de LibreDrop

Sitios estáticos de marketing de LibreDrop y LibreDrop Cloud, hechos con HTML, CSS y JavaScript vanilla (sin frameworks ni dependencias).

## Sitios

| Landing | Carpeta | Dominio | Descripción |
|---------|---------|---------|-------------|
| LibreDrop | `libredrop/` | `https://libredrop.vercel.app` | Plataforma open source |
| LibreDrop Cloud | `libredrop_cloud/` | `https://libredrop-cloud.vercel.app` | Servicio administrado |

## Estructura

Cada landing es autónoma y contiene sus propios assets:

```
landing/libredrop/
├── index.html      # Página principal
├── css/styles.css  # Estilos
├── js/main.js      # Interacción (menú, animaciones, FAQ)
└── assets/images/  # Imágenes y logos locales
```

## Desarrollo

Abre `index.html` directamente en el navegador o sirve la carpeta con un servidor estático:

```bash
python -m http.server 8000
```

## Enlaces entre sitios

Las landings se enlazan entre sí usando dominios de producción:

- LibreDrop → LibreDrop Cloud: `https://libredrop-cloud.vercel.app/`
- LibreDrop Cloud → LibreDrop: `https://libredrop.vercel.app/`

## Despliegue

Se despliegan en Vercel como sitios estáticos (Root Directory = carpeta de cada landing). Ver [docs/DEPLOYMENT.md](../docs/DEPLOYMENT.md).
