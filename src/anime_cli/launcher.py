import sys
import platform
from pathlib import Path

def launch_anipy(anipy_cmd: str, args: list, venv_dir: Path):
    """Ejecuta el buscador usando las flags nativas."""
    print(f"\n[*] Ejecutando reproductor con argumentos: {' '.join(args)}")
    
    import subprocess
    import os
    try:
        if platform.system() == "Windows":
            # Agregar la carpeta 'bin' al PATH para que detecte mpv.exe de forma limpia
            bin_dir = Path(__file__).resolve().parent.parent.parent / "bin"
            os.environ["PATH"] += os.pathsep + str(bin_dir)
            
        # Ejecutamos de forma nativa en TODOS los sistemas (Linux y Windows)
        # anipy-cli maneja su propia consola interactiva y acepta parámetros como -q o -s
        subprocess.call([anipy_cmd] + args)
        
    except KeyboardInterrupt:
        print("\n[!] Has cancelado la ejecución. ¡Hasta pronto!")
    except Exception as e:
        print(f"\n[X] Error durante la ejecución de anipy-cli: {e}")
