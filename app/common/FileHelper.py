"""
Helper para Gestión de Archivos (Con Validación de Formatos y Soporte para Llaves)
==================================================================================
Ubicación: app/common/FileHelper.py
"""
from PyQt6.QtWidgets import QFileDialog, QMessageBox
import os

class FileHelper:
    
    # 1. ACTUALIZADO: Lista maestra de formatos permitidos (.txt y .key)
    EXTENSIONES_PERMITIDAS = ['.txt', '.key']

    @staticmethod
    def abrir_archivo(parent_window):
        """
        Abre un explorador, VALIDA la extensión y devuelve el contenido.
        Permite seleccionar archivos .txt y .key
        """
        # 2. ACTUALIZADO: Filtro visual para ver ambos tipos de archivo
        filtros = "Archivos de Seguridad (*.txt *.key);;Archivos de Texto (*.txt);;Llaves de Seguridad (*.key);;Todos los archivos (*)"
        
        ruta_archivo, _ = QFileDialog.getOpenFileName(
            parent_window,
            "Seleccionar Archivo",
            "",
            filtros
        )

        # Si el usuario canceló (no seleccionó nada)
        if not ruta_archivo:
            return None, None

        # ====================================================================
        # ZONA DE VALIDACIÓN
        # ====================================================================
        # Extraemos la extensión del archivo
        _, extension = os.path.splitext(ruta_archivo)
        
        # Convertimos a minúsculas para comparar ('.TXT' == '.txt')
        extension = extension.lower()

        if extension not in FileHelper.EXTENSIONES_PERMITIDAS:
            # Aquí atrapamos al usuario intentando subir un archivo no permitido
            QMessageBox.warning(
                parent_window,
                "Formato No Soportado",
                f"El archivo seleccionado ({extension}) no es compatible.\n\n"
                f"Solo se permiten formatos: {', '.join(FileHelper.EXTENSIONES_PERMITIDAS)}"
            )
            return None, None

        # ====================================================================
        # LECTURA SEGURA
        # ====================================================================
        try:
            # Si llegamos aquí, sabemos que es una extensión válida
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                return contenido, ruta_archivo
                
        except UnicodeDecodeError:
            # Esto pasa si suben un archivo binario (imagen) renombrado
            QMessageBox.critical(parent_window, "Error de Lectura", "El archivo parece estar dañado o no es texto válido.")
            return None, None
        except Exception as e:
            QMessageBox.critical(parent_window, "Error", f"No se pudo leer el archivo:\n{str(e)}")
            return None, None

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
                return ruta_archivo
            except Exception as e:
                QMessageBox.critical(parent_window, "Error", f"No se pudo guardar el archivo:\n{str(e)}")
                return None
        return None

    @staticmethod
    def guardar_llave_automatica(parent_window, ruta_archivo_origen, contenido_llave):
        """
        Crea una carpeta 'keys' y guarda la llave con el mismo nombre del archivo.
        """
        try:
            # 1. Obtener la carpeta base donde está corriendo la app
            carpeta_base = os.getcwd() 
            carpeta_keys = os.path.join(carpeta_base, "keys")

            # 2. Crear la carpeta 'keys' si no existe
            if not os.path.exists(carpeta_keys):
                os.makedirs(carpeta_keys)

            # 3. Definir el nombre de la llave
            # Si el archivo es "nota.txt", la llave será "keys/nota.txt.key"
            nombre_archivo = os.path.basename(ruta_archivo_origen)
            nombre_llave = f"{nombre_archivo}.key"
            ruta_llave = os.path.join(carpeta_keys, nombre_llave)

            # 4. Guardar la llave automáticamente
            with open(ruta_llave, 'w', encoding='utf-8') as archivo:
                archivo.write(contenido_llave)

            QMessageBox.information(
                parent_window, 
                "Llave Guardada", 
                f"La llave de seguridad se guardó automáticamente en:\n\n{ruta_llave}\n\n¡No borres esta carpeta!"
            )
            return True

        except Exception as e:
            QMessageBox.critical(parent_window, "Error Crítico", f"No se pudo guardar la llave automática:\n{str(e)}")
            return False