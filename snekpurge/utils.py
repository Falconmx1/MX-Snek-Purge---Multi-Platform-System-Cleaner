"""
Utilidades para MX-Snek-Purge
"""

import os
import shutil
import platform
from colorama import Fore, Style
import psutil

def print_banner():
    """Imprime el banner del programa"""
    banner = f"""
{Fore.RED}    ╔══════════════════════════════════════════╗
{Fore.RED}    ║  {Fore.YELLOW}🐍 {Fore.GREEN}MX-Snek-Purge {Fore.CYAN}v1.0.0{Fore.RED}         ║
{Fore.RED}    ║  {Fore.WHITE}¡Limpia tu sistema como una serpiente!{Fore.RED} ║
{Fore.RED}    ╚══════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)

def get_system_info():
    """Obtiene información del sistema"""
    try:
        # Obtener espacio en disco
        disk_usage = shutil.disk_usage("/" if platform.system() != "Windows" else "C:\\")
        free_gb = disk_usage.free / (1024 ** 3)
        total_gb = disk_usage.total / (1024 ** 3)
        return f"{free_gb:.1f} GB libres de {total_gb:.1f} GB"
    except:
        return "No disponible"

def get_size(start_path):
    """Calcula el tamaño de una carpeta o archivo en MB"""
    try:
        if os.path.isfile(start_path):
            return os.path.getsize(start_path) / (1024 * 1024)
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                try:
                    total_size += os.path.getsize(fp)
                except:
                    pass
        return total_size / (1024 * 1024)
    except:
        return 0

def remove_path(path):
    """Elimina un archivo o directorio de forma segura"""
    try:
        if os.path.isfile(path):
            os.remove(path)
            return True
        elif os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
            return True
    except:
        return False
    return False

def format_size(size_mb):
    """Formatea el tamaño en una unidad legible"""
    if size_mb > 1024:
        return f"{size_mb/1024:.2f} GB"
    elif size_mb > 1:
        return f"{size_mb:.2f} MB"
    else:
        return f"{size_mb*1024:.2f} KB"
