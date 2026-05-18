# neowind (Clon Nativo de ani-cli en Python) 🍿

Una potente herramienta de línea de comandos (CLI) multiplataforma que te permite buscar y reproducir anime directamente desde tu terminal de forma rápida y sencilla. Es una alternativa minimalista en Python inspirada en `ani-cli`.

## ✨ Características
- **Multiplataforma:** Total compatibilidad con Windows y distribuciones Linux.
- **Aislado y Limpio:** Crea automáticamente un entorno virtual (`.ani-cli-env`) en tu sistema para no ensuciar tus dependencias globales de Python ni generar errores con PEP-668 en distribuciones recientes.
- **Búsqueda Instantánea:** Pasa el término de búsqueda directamente como argumento.
- **Automatizado:** Saltea los menús tediosos automáticamente gracias a una integración transparente con el motor TUI.

## 🚀 Requisitos Prerevios
1. **Python 3.8+** instalado en tu sistema.
2. Un reproductor de video compatible instalado (`mpv` o `vlc`). 
   - Recomendamos encarecidamente instalar [mpv](https://mpv.io/installation/).

## 💻 Instalación y Uso

No necesitas hacer configuraciones complejas. Solo clona este repositorio o descarga `anime.py` y ejecútalo.

```bash
# Uso básico:
python run.py "nombre del anime"

# Uso avanzado (Calidad, Sub/Dub, y atajos de búsqueda):
python run.py "bleach" -q 1080             # Especificar calidad (1080, 720, best, worst)
python run.py -so "jujutsu kaisen"         # Forzar solo subtítulos (-so)
python run.py -d "dragon ball"             # Forzar doblaje (-d)
python run.py -s "bleach:1-5:sub"          # Saltar menús: Buscar anime, rango de episodios y formato
```

El script se encargará automáticamente de revisar e instalar en segundo plano las dependencias (como `anipy-cli`) durante la primera ejecución.

## 🛠 ¿Cómo funciona bajo el capó?
El núcleo de la aplicación utiliza [anipy-cli](https://github.com/anipy-cli/anipy-cli) como motor robusto de búsqueda y reproducción. Este script modular (`run.py` invoca al paquete en `src/anime_cli/`) asume el rol de Wrapper inyectando de forma nativa los argumentos del sistema (mediante `subprocess`) hacia el CLI de anipy. De esta forma la integración con la terminal original es perfecta, permitiendo comandos complejos y uso multiplataforma (Windows y Linux) sin depender de librerías extrañas de automatización de TTY. Adicionalmente, el script gestiona de forma oculta y silenciosa las rutas relativas para ubicar el reproductor `mpv.exe` dentro de su propio entorno.

##  Contribuciones
¡Las propuestas de mejora, ideas y pull requests de cualquier índole son 100% bienvenidos! Siéntete libre de clonar y testear mejoras, sobre todo en manejo de excepciones de terminal para Windows.

---
⭐ *Si te fue útil esta herramienta sencilla, no olvides dejar tu estrellita en el repositorio.*
