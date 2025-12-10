"""
Lógica de Desencriptación
=====================================
Archivo: app/desencriptacion/controller/desencriptarLogic.py
"""

import sys
import os # Necesario para buscar rutas
from PyQt6.QtWidgets import QApplication, QMessageBox

from desencriptacion.views.DesencriptarWindow import DesencriptarWindow
from common.FileHelper import FileHelper
from encriptacion.tools.AesCipher import AesCipher 

class DesencriptarLogic(DesencriptarWindow):
    def __init__(self):
        super().__init__()
        self.inicializar_logica()
        self.ruta_archivo_actual = None # Para recordar la ruta del archivo cargado

    def inicializar_logica(self):
        self.ui.btnCargarArchivo.clicked.connect(self.cargar_archivo)
        self.ui.btnDesencriptar.clicked.connect(self.desencriptar_mensaje)
        self.ui.btnDescargar.clicked.connect(self.descargar_archivo)
        self.ui.btnRegresar.clicked.connect(self.regresar_menu)

    # ========================================================================
    # FUNCIONES DEL NEGOCIO
    # ========================================================================

    def cargar_archivo(self):
        """
        Carga el archivo y VALIDA si parece estar encriptado.
        """
        # 1. Obtenemos contenido y ruta
        contenido, ruta = FileHelper.abrir_archivo(self)
        
        if contenido is not None:
            # --- VALIDACIÓN INTELIGENTE ---
            # Los archivos de Fernet SIEMPRE empiezan con "gAAAAA"
            if not contenido.startswith("gAAAAA"):
                QMessageBox.warning(
                    self, 
                    "Archivo Sospechoso", 
                    "¡Cuidado!\n\nEste archivo NO parece estar encriptado. O \nEl contenido es legible o tiene un formato incorrecto."
                )
                return
            self.ui.txtMensajeEncriptado.setText(contenido)
            self.ruta_archivo_actual = ruta # Guardamos la ruta para buscar la llave luego

    def desencriptar_mensaje(self):
        texto_encriptado_str = self.ui.txtMensajeEncriptado.toPlainText()
        
        if not texto_encriptado_str:
            QMessageBox.warning(self, "Advertencia", "Primero carga un archivo.")
            return

        # --- VALIDACIÓN PREVIA ---
        if not texto_encriptado_str.startswith("gAAAAA"):
             QMessageBox.critical(self, "Error", "No se puede desencriptar: El texto no tiene formato de encriptación válido.")
             return

        contenido_llave = None
        
        # --------------------------------------------------------------------
        # 1. BÚSQUEDA AUTOMÁTICA DE LLAVE
        # --------------------------------------------------------------------
        if self.ruta_archivo_actual:
            # Armamos la ruta teórica: keys/nombre.txt.key
            nombre_archivo = os.path.basename(self.ruta_archivo_actual)
            carpeta_base = os.getcwd()
            ruta_llave_auto = os.path.join(carpeta_base, "keys", f"{nombre_archivo}.key")
            
            if os.path.exists(ruta_llave_auto):
                try:
                    with open(ruta_llave_auto, 'r', encoding='utf-8') as f:
                        contenido_llave = f.read()
                except:
                    contenido_llave = None

        # --------------------------------------------------------------------
        # 2. BÚSQUEDA MANUAL (Solo Si falla la automática)
        # --------------------------------------------------------------------
        if contenido_llave is None:
            QMessageBox.information(
                self, 
                "Llave Requerida", 
                "No encontramos la llave automáticamente en la carpeta 'keys'.\n\n"
                "Por favor selecciónala manualmente."
            )
            # Ignoramos la ruta de la llave, solo queremos el contenido
            contenido_llave, _ = FileHelper.abrir_archivo(self)
        
        if not contenido_llave:
            return # Cancelado por usuario

        # --------------------------------------------------------------------
        # 3. PROCESO DE DESENCRIPTACIÓN
        # --------------------------------------------------------------------
        try:
            llave_bytes = contenido_llave.encode('utf-8')
            cifrador = AesCipher(llave_bytes)
            
            datos_encriptados = texto_encriptado_str.encode('utf-8')
            texto_plano = cifrador.desencriptar(datos_encriptados)
            
            self.ui.txtMensajeEncriptado.setText(texto_plano)
            QMessageBox.information(self, "Éxito", "Mensaje recuperado correctamente.")
            
        except Exception as e:
            QMessageBox.critical(self, "Error Fatal", "La llave es incorrecta o el archivo está corrupto.")

    def descargar_archivo(self):
        contenido = self.ui.txtMensajeEncriptado.toPlainText()
        FileHelper.guardar_archivo_txt(self, contenido)

    def regresar_menu(self):
        from homePage.menu import MenuWindow
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DesencriptarLogic()
    window.show()
    sys.exit(app.exec())