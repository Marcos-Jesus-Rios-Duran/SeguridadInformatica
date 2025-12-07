"""
Helper para Gestión de Archivos
===============================
Ubicación: app/common/FileHelper.py

Responsabilidad:
    - Abrir cuadros de diálogo del sistema (QFileDialog).
    - Leer contenido de archivos .txt.
    - Guardar contenido en archivos .txt.
"""
from PyQt6.QtWidgets import QFileDialog, QMessageBox
import os

class FileHelper:
    
    @staticmethod
    def abrir_archivo_txt(parent_window):
        """
        Abre un explorador para seleccionar un archivo .txt y devuelve su contenido.
        
        Args:
            parent_window: La ventana que llama (para centrar el diálogo).
            
        Returns:
            str: El contenido del archivo si se seleccionó, None si se canceló.
        """
        ruta_archivo, _ = QFileDialog.getOpenFileName(
            parent_window,
            "Seleccionar Archivo",
            "", # Directorio inicial (vacío = default del sistema)
            "Archivos de Texto (*.txt);;Todos los archivos (*)"
        )

        if ruta_archivo:
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                    contenido = archivo.read()
                    return contenido
            except Exception as e:
                QMessageBox.critical(parent_window, "Error", f"No se pudo leer el archivo:\n{str(e)}")
                return None
        return None

    @staticmethod
    def guardar_archivo_txt(parent_window, contenido):
        """
        Abre un explorador para 'Guardar Como' y escribe el contenido.
        
        Args:
            parent_window: La ventana que llama.
            contenido (str): El texto a guardar.
        """
        if not contenido:
            QMessageBox.warning(parent_window, "Advertencia", "No hay contenido para guardar.")
            return

        ruta_archivo, _ = QFileDialog.getSaveFileName(
            parent_window,
            "Guardar Archivo",
            "",
            "Archivos de Texto (*.txt)"
        )

        if ruta_archivo:
            try:
                # Aseguramos que tenga la extensión .txt
                if not ruta_archivo.endswith('.txt'):
                    ruta_archivo += '.txt'
                
                with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                    archivo.write(contenido)
                
                QMessageBox.information(parent_window, "Éxito", "Archivo guardado correctamente.")
            except Exception as e:
                QMessageBox.critical(parent_window, "Error", f"No se pudo guardar el archivo:\n{str(e)}")