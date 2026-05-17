import sys
from pathlib import Path
from src.anime_cli.env_manager import ensure_venv, install_dependencies
from src.anime_cli.launcher import launch_anipy

def main():
    if len(sys.argv) < 2:
        print("========================================")
        print(" Uso: python run.py \"<nombre_del_anime>\"")
        print(" Ejemplo: python run.py \"bleach\"")
        print("========================================")
        sys.exit(1)
        
    query = " ".join(sys.argv[1:])
    
    # Prepara el entorno
    home_dir = Path.home()
    venv_dir = ensure_venv(home_dir)
    anipy_cmd = install_dependencies(venv_dir)
    
    # Inicia la herramienta
    launch_anipy(anipy_cmd, query, venv_dir)

if __name__ == "__main__":
    main()
