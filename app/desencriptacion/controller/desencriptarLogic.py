"""
Lógica de Desencriptación
=========================
Archivo: app/desencriptacion/controller/desencriptarLogic.py
"""

import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

# 1. IMPORTAR VISTA Y HELPER
from desencriptacion.views.DesencriptarWindow import DesencriptarWindow
from common.FileHelper import FileHelper

# 2. IMPORTAR LA HERRAMIENTA DE ENCRIPTACIÓN (Reutilizamos la misma)
# Nota: Apunta a donde tengas tu AesCipher.py
from encriptacion.tools.AesCipher import AesCipher 

class DesencriptarLogic(DesencriptarWindow):
    def __init__(self):
        super().__init__()
        self.inicializar_logica()

    def inicializar_logica(self):
        self.ui.btnCargarArchivo.clicked.connect(self.cargar_archivo)
        self.ui.btnDesencriptar.clicked.connect(self.desencriptar_mensaje)
        self.ui.btnDescargar.clicked.connect(self.descargar_archivo)
        self.ui.btnRegresar.clicked.connect(self.regresar_menu)

    # ========================================================================
    # FUNCIONES DEL NEGOCIO
    # ========================================================================

    def cargar_archivo(self):
        """Usa el FileHelper para cargar el texto cifrado."""
        contenido = FileHelper.abrir_archivo(self)
        if contenido is not None:
            self.ui.txtMensajeEncriptado.setText(contenido)

    def desencriptar_mensaje(self):
        """
        Pide la llave, inicializa el Cifrador y revela el mensaje.
        """
        # 1. Obtener el texto encriptado de la pantalla
        texto_encriptado_str = self.ui.txtMensajeEncriptado.toPlainText()
        
        if not texto_encriptado_str:
            QMessageBox.warning(self, "Advertencia", "Primero carga un archivo encriptado.")
            return

        # 2. PEDIR LA LLAVE AL USUARIO
        # Le decimos al usuario que busque su archivo .key
        QMessageBox.information(self, "Requerido", "Para desencriptar, necesitamos tu LLAVE DE SEGURIDAD (.key).\n\nSelecciónala en la siguiente ventana (Revisa la carpeta 'keys').")
        
        contenido_llave = FileHelper.abrir_archivo(self)
        
        if not contenido_llave:
            return # El usuario canceló o no cargó nada

        # 3. PROCESO DE DESENCRIPTACIÓN
        try:
            # Convertimos la llave de texto a bytes (formato que pide la librería)
            llave_bytes = contenido_llave.encode('utf-8')
            
            # Instanciamos tu herramienta con la llave cargada
            cifrador = AesCipher(llave_bytes)
            
            # Convertimos el mensaje de la pantalla a bytes
            datos_encriptados = texto_encriptado_str.encode('utf-8')
            
            # ¡MAGIA! Desencriptamos
            texto_plano = cifrador.desencriptar(datos_encriptados)
            
            # 4. Mostrar el resultado
            self.ui.txtMensajeEncriptado.setText(texto_plano)
            
            QMessageBox.information(self, "Éxito", "El mensaje ha sido desencriptado correctamente.")
            
        except Exception as e:
            # Si la llave no es la correcta, AesCipher fallará y caeremos aquí
            QMessageBox.critical(self, "Error de Desencriptación", "No se pudo desencriptar.\n\nPosibles causas:\n1. La llave seleccionada NO corresponde a este archivo.\n2. El archivo está dañado.")

    def descargar_archivo(self):
        """Guarda el resultado (ya desencriptado)."""
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