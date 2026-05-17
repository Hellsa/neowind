import sys
import subprocess
from pathlib import Path
import platform
import os

def get_venv_command(venv_dir: Path, cmd: str) -> str:
    """Devuelve la ruta absoluta del comando para usar dentro del entorno virtual en Linux o Windows."""
    if platform.system() == "Windows":
        cmd_name = f"{cmd}.exe" if not cmd.startswith("pip") else "pip.exe"
        cmd_path = venv_dir / "Scripts" / cmd_name
        if not cmd_path.exists():
            cmd_path = venv_dir / "Scripts" / f"{cmd}.exe"
            if not cmd_path.exists(): 
                cmd_path = venv_dir / "Scripts" / cmd
    else:
        cmd_path = venv_dir / "bin" / cmd
    return str(cmd_path)

def ensure_venv(home: Path) -> Path:
    """Crea el entorno virtual si no existe."""
    import venv
    venv_dir = home / ".ani-cli-env"
    
    if not venv_dir.exists():
        print(f"[*] Creando entorno virtual aislado en {venv_dir}...")
        print("[*] Esto evita que manchemos tu sistema global con dependencias de python.")
        try:
            venv.create(venv_dir, with_pip=True)
        except Exception as e:
            print(f"[X] Fallo al crear el entorno virtual: {e}")
            sys.exit(1)
    return venv_dir

def install_dependencies(venv_dir: Path):
    """Verifica e instala los paquetes base en el entorno aislado si no se encuentran."""
    anipy_cmd = get_venv_command(venv_dir, "anipy-cli")
    pip_cmd = get_venv_command(venv_dir, "pip")
    
    if not os.path.exists(anipy_cmd) and not os.path.exists(anipy_cmd + ".exe"):
        print("\n[*] Instalando el motor de búsqueda y scraping ('anipy-cli') por primera vez...")
        print("[*] (Tomará unos segundos dependiendo de tu conexión)\n")
        try:
            subprocess.check_call([pip_cmd, "install", "--upgrade", "pip", "setuptools", "wheel"])
            subprocess.check_call([pip_cmd, "install", "anipy-cli", "pexpect", "wepexpect"])
            print("\n[+] Motor instalado correctamente.\n")
        except subprocess.CalledProcessError as e:
            print(f"\n[X] Hubo un error instalando las dependencias. Verifica tu conexión a internet o compiladores del sistema.")
            sys.exit(1)
            
    return anipy_cmd
