# Contribuir a LibreDrop

¡Gracias por tu interés en contribuir a LibreDrop! Este es un proyecto open-source (AGPLv3) hecho en Guatemala para dropshipping soberano.

## Cómo empezar

1. Haz un fork del repositorio.
2. Clona tu fork: `git clone git@github.com:<tu-usuario>/LibreDrop.git`
3. Crea y activa un entorno virtual: `python -m venv .venv && source .venv/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Crea una rama para tu contribución: `git checkout -b mi-cambio`

## Entorno de desarrollo

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

Actualmente el backend usa Django con Python.

## Estándares de código

- Usa Python 3.12+ para todo el código nuevo.
- Sigue las convenciones del código existente.
- No agregues comentarios innecesarios.
- Mantén las funciones pequeñas y con un solo propósito.
- Sigue PEP 8 para el estilo de código.

## Commits

- Usa mensajes claros y descriptivos en español o inglés.
- Prefiere commits pequeños y atómicos.

## Pull Requests

1. Asegúrate de que tu código funcione correctamente.
2. Describe claramente qué cambia y por qué.
3. Referencia cualquier issue relevante.
4. Un mantenedor revisará tu PR lo antes posible.

## Reportar issues

- Usa el [rastreador de issues](https://github.com/Sebas16608/LibreDrop/issues) de GitHub.
- Incluye pasos para reproducir el problema si aplica.
- Menciona tu sistema operativo y versión de Python.

## Código de conducta

Sé respetuoso y constructivo. Este es un proyecto comunitario y todas las contribuciones son bienvenidas.

## Licencia

Al contribuir, aceptas que tu código será distribuido bajo la licencia AGPLv3.