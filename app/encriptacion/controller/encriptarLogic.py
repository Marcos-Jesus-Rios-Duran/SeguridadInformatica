"""
Lógica de Encriptación
======================
Archivo: app/encriptacion/encriptarLogic.py

Responsabilidad:
    - Heredar la vista compuesta (EncriptarWindowUI)
    - Dar funcionalidad a los botones (Encriptar, Enviar, Regresar).
"""

import sys
from PyQt6.QtWidgets import QApplication

from encriptacion.views.EncriptarWindow import EncriptarWindowUI

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

    # ========================================================================
    # FUNCIONES DEL NEGOCIO (Aquí va tu código inteligente)
    # ========================================================================

    def encriptar_mensaje(self):
        print("Lógica: Iniciando proceso de encriptación...")
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