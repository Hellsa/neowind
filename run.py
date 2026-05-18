import sys
from pathlib import Path
from src.anime_cli.env_manager import ensure_venv, install_dependencies
from src.anime_cli.launcher import launch_anipy

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("========================================")
        print(" Uso básico: python run.py \"<nombre_del_anime>\"")
        print(" Uso avanzado: python run.py \"bleach\" -q 1080")
        print("               python run.py -s \"bleach:1-10:sub\"")
        print("========================================")
        sys.exit(1)
        
    # Prepara el entorno
    home_dir = Path.home()
    venv_dir = ensure_venv(home_dir)
    anipy_cmd = install_dependencies(venv_dir)
    
    # Inicia la herramienta
    launch_anipy(anipy_cmd, args, venv_dir)

if __name__ == "__main__":
    main()
