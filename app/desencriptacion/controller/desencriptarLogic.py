"""
Lógica de Desencriptación
=========================
Archivo: app/desencriptacion/desencriptarLogic.py

Responsabilidad:
    - Heredar la estructura visual (DesencriptarWindow)
    - Dar funcionalidad a los botones (Cargar, Desencriptar, Regresar).
"""

import sys
from PyQt6.QtWidgets import QApplication

# Importamos la ventana compuesta que acabamos de crear arriba
from desencriptacion.views.DesencriptarWindow import DesencriptarWindow

class DesencriptarLogic(DesencriptarWindow):
    """
    Controlador que maneja la lógica de negocio para desencriptar.
    """
    def __init__(self):
        # 1. Construimos la ventana visual
        super().__init__()
        
        # 2. Conectamos los cables (Señales a Funciones)
        self.inicializar_logica()

    def inicializar_logica(self):
        """Conecta los botones de la vista con sus funciones correspondientes."""
        self.ui.btnCargarArchivo.clicked.connect(self.cargar_archivo)
        self.ui.btnDesencriptar.clicked.connect(self.desencriptar_mensaje)
        self.ui.btnDescargar.clicked.connect(self.descargar_archivo)
        self.ui.btnRegresar.clicked.connect(self.regresar_menu)

    # ========================================================================
    # FUNCIONES DEL NEGOCIO (Aquí va la magia)
    # ========================================================================

    def cargar_archivo(self):
        print("Lógica: Abriendo explorador para seleccionar archivo encriptado...")
        # Aquí iría: QFileDialog.getOpenFileName...

    def desencriptar_mensaje(self):
        print("Lógica: Ejecutando algoritmo de desencriptación...")
        # Ejemplo: tomar el texto, procesarlo y mostrarlo
        texto = self.ui.txtMensajeEncriptado.toPlainText()
        # lógica ficticia
        if texto:
            print(f"Procesando: {texto}")
        else:
            print("No hay mensaje cargado.")

    def descargar_archivo(self):
        print("Lógica: Guardando mensaje desencriptado en disco...")

    def regresar_menu(self):
        """Cierra esta ventana y abre el menú principal."""
        # Importación local para evitar ciclos
        from homePage.menu import MenuWindow
        
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.close()

# Bloque para probar solo esta ventana
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DesencriptarLogic() # Importante: Instanciamos la LÓGICA
    window.show()
    sys.exit(app.exec())