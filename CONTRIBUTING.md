# Guía de Contribución 🤝

¡Gracias por mostrar interés en aportar a **Anime.py**! Este proyecto se mantiene vivo gracias al apoyo de una comunidad open source. Ya sea que quieras arreglar un bug, sugerir un feature o corregir un simple error tipográfico, toda ayuda es excelente.

## ¿Cómo colaborar?

### 1. Reportando Bugs (Errores)
Si la herramienta falla (por un cambio en las APIs, caída de reproductores o error de código), por favor abre un **Issue** en la pestaña de GitHub asegurándote de incluir:
- Tu sistema operativo (ej. *Windows 11* o *Arch Linux*).
- Cómo reproducir el error exacto y el log que arroja la terminal.

### 2. Sugiriendo Features
Abrimos debate constante sobre cómo mejorar la TUI o cómo integrarlo con otros reproductores. ¡Abre un Issue comentando tu idea antes de programarla para debatirla y asegurar que se ajusta a nuestro minimalismo!

### 3. Haciendo Pull Requests (PR)
Si deseas agregar tu propio código como mejora al repositorio central:
1. Pica el botón de **Fork** arriba a la derecha en GitHub.
2. Clona el repositorio `git clone https://github.com/tu_usuario/neowin.git`.
3. Crea tu rama para los arreglos: `git checkout -b feature/mi-nueva-idea`
4. Añade tus cambios a `src/anime_cli/`.
5. Haz commit de los pequeños cambios con mensajes claros: `git commit -m "Añadida compatibilidad con reproductor X"`.
6. Haz push a la rama: `git push origin feature/mi-nueva-idea`.
7. Abre un **Pull Request** detallando tus adiciones en la pestaña original de este repo.

## Estilo de Código (Linting)
No tenemos reglas extremadamente robustas. Únicamente pedimos que:
- Mantengas los principios PEP8 de Python dentro de lo posible.
- Mantengas la división del código en la carpeta `src/anime_cli/` sin agrupar miles de líneas en `run.py`.
- ¡Documentes brevemente la función si creas un bloque nuevo complejo!

¡Feliz refactorización! 👨‍💻
