"""
Módulo específico para Linux
"""

import os
import subprocess
import shutil
from pathlib import Path
from ..utils import get_size, remove_path

def clean_cache():
    """Limpia caché en Linux"""
    freed = 0
    cache_paths = [
        "/var/cache",
        "/tmp",
        "/var/tmp",
        os.path.expanduser("~/.cache"),
        os.path.expanduser("~/.thumbnails"),
        os.path.expanduser("~/.local/share/Trash"),
    ]
    
    for path in cache_paths:
        if os.path.exists(path):
            size_before = get_size(path)
            # Limpiar con sudo si es necesario
            try:
                if path.startswith("/var"):
                    subprocess.run(['sudo', 'rm', '-rf', path + '/*'], 
                                 check=False, capture_output=True)
                else:
                    shutil.rmtree(path, ignore_errors=True)
                    os.makedirs(path, exist_ok=True)
                freed += size_before
            except:
                pass
    
    # Limpiar caché de APT
    try:
        if shutil.which('apt-get'):
            result = subprocess.run(['sudo', 'apt-get', 'clean'], 
                                  capture_output=True, text=True)
            # Tamaño aproximado
            freed += 100  # Aproximado
    except:
        pass
    
    return freed

def clean_temp():
    """Limpia archivos temporales en Linux"""
    freed = 0
    temp_paths = [
        "/tmp/*",
        "/var/tmp/*",
        os.path.expanduser("~/.local/share/Trash/*"),
    ]
    
    for path_pattern in temp_paths:
        for path in Path().glob(path_pattern):
            if path.exists():
                freed += get_size(str(path))
                remove_path(str(path))
    
    return freed

def clean_trash():
    """Vacía la papelera en Linux"""
    freed = 0
    trash_paths = [
        os.path.expanduser("~/.local/share/Trash/files"),
        os.path.expanduser("~/.local/share/Trash/info"),
    ]
    
    for path in trash_paths:
        if os.path.exists(path):
            freed += get_size(path)
            remove_path(path)
            os.makedirs(path, exist_ok=True)
    
    return freed

def clean_logs():
    """Limpia logs en Linux"""
    freed = 0
    log_paths = [
        "/var/log/*.log",
        "/var/log/*.1",
        "/var/log/*.gz",
    ]
    
    for path_pattern in log_paths:
        for path in Path().glob(path_pattern):
            if path.exists():
                freed += get_size(str(path))
                try:
                    subprocess.run(['sudo', 'rm', '-f', str(path)], 
                                 check=False, capture_output=True)
                except:
                    pass
    
    # Rotar logs con logrotate
    try:
        if shutil.which('logrotate'):
            subprocess.run(['sudo', 'logrotate', '-f', '/etc/logrotate.conf'],
                         check=False, capture_output=True)
    except:
        pass
    
    return freed

def clean_docker():
    """Limpia caché de Docker"""
    freed = 0
    try:
        if shutil.which('docker'):
            # Limpiar caché de Docker
            subprocess.run(['docker', 'system', 'prune', '-a', '-f'],
                         check=False, capture_output=True)
            # Podemos estimar el espacio liberado
            freed += 200  # Aproximado
    except:
        pass
    return freed

def optimize_swap():
    """Optimiza la memoria swap en Linux"""
    freed = 0
    try:
        # Limpiar swap (desactivar y reactivar)
        subprocess.run(['sudo', 'swapoff', '-a'], check=False, capture_output=True)
        subprocess.run(['sudo', 'swapon', '-a'], check=False, capture_output=True)
        # No podemos medir espacio liberado directamente
        return 0
    except:
        return 0
