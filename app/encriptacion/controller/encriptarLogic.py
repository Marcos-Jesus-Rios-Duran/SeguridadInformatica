"""
Lógica de Encriptación
======================
Archivo: app/encriptacion/encriptarLogic.py

Responsabilidad:
    - Heredar la vista compuesta (EncriptarWindowUI)
    - Dar funcionalidad a los botones (Encriptar, Enviar, Regresar).
"""

import sys
from PyQt6.QtWidgets import QApplication, QMessageBox


from encriptacion.views.EncriptarWindow import EncriptarWindowUI
from common.FileHelper import FileHelper
class EncriptarLogic(EncriptarWindowUI):
    """
    Controlador que maneja la lógica de encriptación.
    """
    def __init__(self):
        # Llamamos al pintor para que construya la ventana
        super().__init__()
        
        # Ahora conectamos los cables (Señales)
        self.inicializar_logica()

    def inicializar_logica(self):
        """Conecta los botones con sus funciones."""
        self.ui.btnEncriptar.clicked.connect(self.encriptar_mensaje)
        self.ui.btnDescargar.clicked.connect(self.descargar_archivo)
        self.ui.btnEnviar.clicked.connect(self.enviar_mensaje)
        self.ui.btnRegresar.clicked.connect(self.regresar_menu)
    # --- NUEVA CONEXIÓN ---
        # Conectamos el botón cargar archivo
        self.ui.btnCargar.clicked.connect(self.cargar_archivo_txt)
    # ========================================================================
    # FUNCIONES DEL NEGOCIO
    # ========================================================================

    def cargar_archivo_txt(self):
        """Usa el FileHelper para leer un TXT y colocarlo en pantalla 

        """
        #Llamada a el helper
        contenido = FileHelper.abrir_archivo(self)
        if contenido is not None:
            self.ui.txtMensaje.setText(contenido)
            QMessageBox.information(self, "Exito","Abierto con exito")

    def encriptar_mensaje(self):
        mensaje = self.ui.txtMensaje.toPlainText()
        if mensaje:
            print(f"Encriptando: {mensaje}")
            # Aquí iría tu algoritmo (AES, RSA, etc.)
        else:
            print("El campo de texto está vacío.")

    def descargar_archivo(self):
        print("Lógica: Guardando archivo encriptado...")
        # Aquí iría el QFileDialog.getSaveFileName

    def enviar_mensaje(self):
        print("Lógica: Preparando envío de correo/mensaje...")

    def regresar_menu(self):
        # Importamos aquí para evitar errores circulares
        from homePage.menu import MenuWindow
        
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.close()

# Para probar solo esta ventana
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EncriptarLogic() # Instanciamos la LÓGICA
    window.show()
    sys.exit(app.exec())