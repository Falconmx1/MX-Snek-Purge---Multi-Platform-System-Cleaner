"""
Módulo de limpieza del sistema
"""

import os
import shutil
import platform
from pathlib import Path
from colorama import Fore, Style
from .platforms import windows, linux

class SystemCleaner:
    """Clase principal para la limpieza del sistema"""
    
    def __init__(self, system, auto_confirm=False):
        self.system = system
        self.auto_confirm = auto_confirm
        self.freed_space = 0
        self.cleaned_items = []
        
        # Seleccionar módulo de plataforma
        if system == "Windows":
            self.platform_module = windows
        elif system in ["Linux", "Darwin"]:
            self.platform_module = linux
        else:
            raise NotImplementedError(f"Sistema no soportado: {system}")
    
    def confirm_action(self, message):
        """Pregunta al usuario si quiere continuar"""
        if self.auto_confirm:
            return True
        response = input(f"{Fore.YELLOW}❓ {message} (y/n): ").strip().lower()
        return response in ['y', 'yes', 's', 'si']
    
    def clean_cache(self):
        """Limpia la caché del sistema"""
        print(f"{Fore.CYAN}🧹 Limpiando caché del sistema...")
        freed = self.platform_module.clean_cache()
        self.freed_space += freed
        self.cleaned_items.append(("Caché del sistema", freed))
        print(f"{Fore.GREEN}✅ Caché limpiada: {Fore.YELLOW}{freed:.2f} MB liberados")
    
    def clean_temp(self):
        """Limpia archivos temporales"""
        print(f"{Fore.CYAN}🗑️  Limpiando archivos temporales...")
        freed = self.platform_module.clean_temp()
        self.freed_space += freed
        self.cleaned_items.append(("Archivos temporales", freed))
        print(f"{Fore.GREEN}✅ Temporales eliminados: {Fore.YELLOW}{freed:.2f} MB liberados")
    
    def clean_trash(self):
        """Vacía la papelera"""
        print(f"{Fore.CYAN}🗑️  Vaciando papelera de reciclaje...")
        freed = self.platform_module.clean_trash()
        self.freed_space += freed
        self.cleaned_items.append(("Papelera", freed))
        print(f"{Fore.GREEN}✅ Papelera vaciada: {Fore.YELLOW}{freed:.2f} MB liberados")
    
    def optimize_swap(self):
        """Optimiza la memoria swap"""
        print(f"{Fore.CYAN}🔄 Optimizando memoria swap...")
        freed = self.platform_module.optimize_swap()
        self.freed_space += freed
        self.cleaned_items.append(("Swap optimizada", freed))
        print(f"{Fore.GREEN}✅ Swap optimizada: {Fore.YELLOW}{freed:.2f} MB liberados")
    
    def clean_logs(self):
        """Limpia logs del sistema"""
        print(f"{Fore.CYAN}📋 Limpiando logs del sistema...")
        freed = self.platform_module.clean_logs()
        self.freed_space += freed
        self.cleaned_items.append(("Logs del sistema", freed))
        print(f"{Fore.GREEN}✅ Logs limpiados: {Fore.YELLOW}{freed:.2f} MB liberados")
    
    def clean_docker(self):
        """Limpia caché de Docker (Linux)"""
        if self.system == "Linux":
            print(f"{Fore.CYAN}🐳 Limpiando caché de Docker...")
            freed = linux.clean_docker()
            self.freed_space += freed
            self.cleaned_items.append(("Docker", freed))
            print(f"{Fore.GREEN}✅ Docker limpiado: {Fore.YELLOW}{freed:.2f} MB liberados")
    
    def full_clean(self):
        """Ejecuta limpieza completa"""
        print(f"{Fore.MAGENTA}🐍 Iniciando limpieza completa...")
        print(f"{Fore.YELLOW}⚠️  Esta operación eliminará archivos temporales y caché")
        
        if not self.auto_confirm:
            if not self.confirm_action("¿Deseas continuar con la limpieza completa?"):
                print(f"{Fore.YELLOW}Limpieza cancelada")
                return
        
        # Ejecutar todas las limpiezas
        self.clean_cache()
        self.clean_temp()
        self.clean_trash()
        self.clean_logs()
        
        if self.system == "Linux":
            self.clean_docker()
        
        self.optimize_swap()
        
        # Mostrar resumen
        self.show_summary()
    
    def get_total_freed(self):
        """Retorna el total de espacio liberado"""
        return self.freed_space
    
    def show_summary(self):
        """Muestra resumen de la limpieza"""
        print()
        print(f"{Fore.CYAN}{'='*50}")
        print(f"{Fore.MAGENTA}📊 RESUMEN DE LIMPIEZA")
        print(f"{Fore.CYAN}{'='*50}")
        
        for item, size in self.cleaned_items:
            print(f"{Fore.WHITE}• {item}: {Fore.GREEN}{size:.2f} MB")
        
        print(f"{Fore.CYAN}{'-'*50}")
        print(f"{Fore.GREEN}✅ Total liberado: {Fore.YELLOW}{self.freed_space:.2f} MB")
        print(f"{Fore.CYAN}{'='*50}")
