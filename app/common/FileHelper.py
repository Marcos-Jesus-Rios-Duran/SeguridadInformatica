"""
Helper para Gestión de Archivos (Con Validación de Formatos)
============================================================
Ubicación: app/common/FileHelper.py
"""
from PyQt6.QtWidgets import QFileDialog, QMessageBox
import os

class FileHelper:
    
    # Lista maestra de formatos permitidos.
    # Ahorita solo TXT, pero aquí agregaremos '.pdf' en el futuro.
    EXTENSIONES_PERMITIDAS = ['.txt']

    @staticmethod
    def abrir_archivo(parent_window):
        """
        Abre un explorador, VALIDA la extensión y devuelve el contenido.
        """
        # 1. Configurar el filtro visual para el diálogo
        # (Esto ayuda al usuario, pero no es la seguridad real)
        filtros = "Archivos de Texto (*.txt);;Todos los archivos (*)"
        
        ruta_archivo, _ = QFileDialog.getOpenFileName(
            parent_window,
            "Seleccionar Archivo",
            "",
            filtros
        )

        # Si el usuario canceló (no seleccionó nada)
        if not ruta_archivo:
            return None

        # ====================================================================
        # ZONA DE VALIDACIÓN (Tu idea)
        # ====================================================================
        # Extraemos la extensión del archivo (ej: 'video.mp4' -> '.mp4')
        _, extension = os.path.splitext(ruta_archivo)
        
        # Convertimos a minúsculas para comparar ('.TXT' == '.txt')
        extension = extension.lower()

        if extension not in FileHelper.EXTENSIONES_PERMITIDAS:
            # Aquí atrapamos al usuario intentando subir un video o imagen
            QMessageBox.warning(
                parent_window,
                "Formato No Soportado",
                f"El archivo seleccionado ({extension}) no es compatible.\n\n"
                f"Solo se permiten formatos: {', '.join(FileHelper.EXTENSIONES_PERMITIDAS)}"
            )
            return None

        # ====================================================================
        # LECTURA SEGURA
        # ====================================================================
        try:
            # Si llegamos aquí, sabemos que es una extensión válida (.txt)
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                return contenido
                
        except UnicodeDecodeError:
            # Esto pasa si suben un archivo binario (imagen) renombrado a .txt
            QMessageBox.critical(parent_window, "Error de Lectura", "El archivo parece estar dañado o no es texto válido.")
            return None
        except Exception as e:
            QMessageBox.critical(parent_window, "Error", f"No se pudo leer el archivo:\n{str(e)}")
            return None

    @staticmethod
    def guardar_archivo_txt(parent_window, contenido):
        """
        Guarda contenido en un archivo .txt
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
                if not ruta_archivo.endswith('.txt'):
                    ruta_archivo += '.txt'
                
                with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                    archivo.write(contenido)
                
                QMessageBox.information(parent_window, "Éxito", "Archivo guardado correctamente.")
            except Exception as e:
                QMessageBox.critical(parent_window, "Error", f"No se pudo guardar el archivo:\n{str(e)}")