#!/usr/bin/env python3
"""
Módulo principal de MX-Snek-Purge
"""

import os
import sys
import platform
import argparse
from colorama import init, Fore, Style
from .cleaner import SystemCleaner
from .utils import print_banner, get_system_info

init(autoreset=True)

def main():
    """Función principal del programa"""
    parser = argparse.ArgumentParser(
        description="MX-Snek-Purge - Limpieza y optimización del sistema"
    )
    parser.add_argument(
        "--auto", 
        action="store_true",
        help="Modo automático sin confirmación"
    )
    parser.add_argument(
        "--cache", 
        action="store_true",
        help="Solo limpiar caché"
    )
    parser.add_argument(
        "--temp", 
        action="store_true",
        help="Solo limpiar archivos temporales"
    )
    parser.add_argument(
        "--swap", 
        action="store_true",
        help="Solo optimizar swap"
    )
    parser.add_argument(
        "--version", 
        action="version",
        version="MX-Snek-Purge v1.0.0"
    )
    
    args = parser.parse_args()
    
    # Mostrar banner
    print_banner()
    
    # Información del sistema
    system = platform.system()
    print(f"{Fore.CYAN}🔍 Sistema detectado: {Fore.YELLOW}{system}")
    print(f"{Fore.CYAN}💾 Espacio disponible: {Fore.GREEN}{get_system_info()}")
    print()
    
    # Inicializar cleaner
    cleaner = SystemCleaner(system, auto_confirm=args.auto)
    
    try:
        # Limpiar según argumentos
        if args.cache:
            cleaner.clean_cache()
        elif args.temp:
            cleaner.clean_temp()
        elif args.swap:
            cleaner.optimize_swap()
        else:
            # Limpieza completa
            cleaner.full_clean()
            
        # Mostrar resumen final
        print()
        print(f"{Fore.GREEN}✅ ¡Limpieza completada con éxito!")
        print(f"{Fore.CYAN}📊 Espacio liberado total: {Fore.YELLOW}{cleaner.get_total_freed()} MB")
        print(f"{Fore.CYAN}💾 Espacio disponible ahora: {Fore.GREEN}{get_system_info()}")
        print()
        print(f"{Fore.MAGENTA}🐍 ¡Tu sistema está más ligero que una serpiente!")
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}⚠️  Operación cancelada por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}❌ Error: {str(e)}")
        sys.exit(1)
    
    return 0

if __name__ == "__main__":
    main()
