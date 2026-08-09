# 🐍 MX-Snek-Purge

> *"Limpia tu sistema como una serpiente muda de piel"*

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-green.svg)](https://github.com)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

## 📋 Descripción

**MX-Snek-Purge** es una herramienta de línea de comandos diseñada para limpiar y optimizar tu sistema operativo. Desarrollada en Python, es multiplataforma y funciona tanto en Windows como en Linux.

### ✨ Características

- 🧹 **Limpieza de caché**: Elimina caché del sistema, navegadores y aplicaciones
- 💾 **Liberación de espacio**: Borra archivos temporales, logs, y basura del sistema
- 🔄 **Optimización de swap**: Limpia y optimiza la memoria swap
- 🗑️ **Eliminación segura**: Papelera, archivos duplicados y temporales
- 📊 **Estadísticas**: Muestra cuánto espacio has liberado
- 🎨 **Interfaz colorida**: Salida bonita y legible en la terminal
- 🛡️ **Modo seguro**: Confirmación antes de eliminar archivos importantes

## 🚀 Instalación

### Clonar el repositorio
```bash
git clone https://github.com/Falconmx1/MX-Snek-Purge.git
cd MX-Snek-Purge

Instalar dependencias

pip install -r requirements.txt
Instalar como paquete (opcional)

pip install -e .
💻 Uso
Ejecución básica

# Modo interactivo (recomendado)
python snekpurge.py

# Modo automático (sin confirmación)
python snekpurge.py --auto

# Solo limpiar caché
python snekpurge.py --cache

# Solo limpiar archivos temporales
python snekpurge.py --temp

# Solo optimizar swap
python snekpurge.py --swap

# Mostrar ayuda
python snekpurge.py --help
Ejemplos

# Limpieza completa con confirmación
$ python snekpurge.py
🐍 MX-Snek-Purge iniciado...
Detectando sistema operativo: Linux
Espacio disponible antes: 45.2 GB
¿Limpiar caché del sistema? (y/n): y
✅ Caché eliminada: 1.8 GB liberados
...
Total liberado: 3.4 GB

🖥️ Plataformas Soportadas
Sistema Operativo             Versión             Estado
Windows                       10, 11              ✅ Soportado
Linux (Debian/Ubuntu)         18.04+              ✅ Soportado
Linux (Fedora)                35+                 ✅ Soportado
Linux (Arch)                  Rolling             ✅ Soportado

⚙️ Dependencias
Python 3.8+

colorama (para colores en terminal)

psutil (para información del sistema)

(Opcional) tqdm (para barras de progreso)
