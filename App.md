# Generación del Ejecutable (.exe) - CriptoApp v1.0

Este documento detalla el proceso técnico utilizado para compilar la aplicación Python (`.py`) en un archivo ejecutable independiente (`.exe`) para Windows, permitiendo su distribución sin necesidad de que el usuario final tenga Python instalado.

## 📋 Prerrequisitos

Antes de generar el ejecutable, se aseguró que el entorno virtual tuviera instaladas todas las dependencias necesarias y la herramienta de compilación.

1.  **Dependencias del Proyecto:**
    * `PyQt6`: Interfaz gráfica.
    * `cryptography`: Lógica de encriptación AES.
2.  **Herramienta de Compilación:**
    * `pyinstaller`: Empaquetador de aplicaciones Python.

```bash
pip install pyinstaller