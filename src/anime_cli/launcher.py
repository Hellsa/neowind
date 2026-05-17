import sys
import platform
from pathlib import Path

def launch_anipy(anipy_cmd: str, query: str, venv_dir: Path):
    """Automatiza el bypass de interfaz para ingresar directamente al buscador."""
    print(f"\n[*] Ejecutando reproductor y buscando: {query}")
    print("[*] Escribe el número del anime deseado en el menú que aparecerá.\n")
    
    try:
        if platform.system() == "Windows":
            import wepexpect as pexpect_mod
        else:
            site_packages_matches = list((venv_dir / "lib").glob("python*/site-packages"))
            if site_packages_matches:
                sys.path.append(str(site_packages_matches[0]))
            import pexpect as pexpect_mod

        child = pexpect_mod.spawn(anipy_cmd, timeout=3, encoding='utf-8')
        
        # Saltar prompt genérico "en temporada"
        try:
            child.expect(r'\? Do you want to search in season', timeout=3)
            child.sendline('n')
        except pexpect_mod.TIMEOUT:
            pass

        # Inyectar el texto a buscar
        try:
            child.expect(r'Search anime:', timeout=3)
            child.sendline(query)
        except pexpect_mod.TIMEOUT:
            pass
            
        # Devolver el control interactivo al humano
        child.interact()
        
    except KeyboardInterrupt:
        print("\n[!] Has cancelado la ejecución. ¡Hasta pronto!")
    except Exception as e:
        print(f"\n[X] Error durante la ejecución del proceso interno: {e}")
