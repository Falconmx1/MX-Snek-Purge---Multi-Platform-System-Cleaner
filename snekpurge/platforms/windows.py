"""
Módulo específico para Windows
"""

import os
import shutil
import subprocess
from pathlib import Path
from ..utils import get_size, remove_path

def clean_cache():
    """Limpia caché en Windows"""
    freed = 0
    cache_paths = [
        os.path.expandvars(r"%USERPROFILE%\AppData\Local\Temp"),
        os.path.expandvars(r"%USERPROFILE%\AppData\Local\Microsoft\Windows\INetCache"),
        os.path.expandvars(r"%USERPROFILE%\AppData\Local\Google\Chrome\User Data\Default\Cache"),
        os.path.expandvars(r"%USERPROFILE%\AppData\Local\Mozilla\Firefox\Profiles\*\cache2"),
    ]
    
    for path_pattern in cache_paths:
        for path in Path().glob(path_pattern.replace("\\", "/")):
            if path.exists():
                freed += get_size(str(path))
                remove_path(str(path))
    
    return freed

def clean_temp():
    """Limpia archivos temporales en Windows"""
    freed = 0
    temp_paths = [
        os.path.expandvars(r"%TEMP%"),
        os.path.expandvars(r"%TMP%"),
        os.path.expandvars(r"%WINDIR%\Temp"),
        os.path.expandvars(r"%USERPROFILE%\Downloads"),
    ]
    
    for path in temp_paths:
        if os.path.exists(path):
            freed += get_size(path)
            remove_path(path)
    
    return freed

def clean_trash():
    """Vacía la papelera en Windows"""
    freed = 0
    try:
        # Usar PowerShell para vaciar papelera
        cmd = ['powershell', '-Command', 
               'Clear-RecycleBin -Force -ErrorAction SilentlyContinue']
        result = subprocess.run(cmd, capture_output=True, text=True)
        # No podemos obtener el tamaño exacto fácilmente
        return 0
    except:
        return 0

def clean_logs():
    """Limpia logs en Windows"""
    freed = 0
    log_paths = [
        os.path.expandvars(r"%WINDIR%\Logs"),
        os.path.expandvars(r"%USERPROFILE%\AppData\Local\Temp\*.log"),
    ]
    
    for path_pattern in log_paths:
        for path in Path().glob(path_pattern.replace("\\", "/")):
            if path.exists():
                freed += get_size(str(path))
                remove_path(str(path))
    
    return freed

def optimize_swap():
    """Optimiza swap en Windows (no implementado)"""
    return 0
