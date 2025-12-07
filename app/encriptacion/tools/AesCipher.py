"""
Herramienta de Cifrado AES (Simétrico)
======================================
Ubicación: app/encriptacion/tools/AesCipher.py

Responsabilidad:
    - Generar llaves de encriptación.
    - Encriptar texto plano.
    - Desencriptar texto cifrado.
    - NO sabe nada de la interfaz gráfica.
"""
from cryptography.fernet import Fernet

class AesCipher:
    
    def __init__(self, key=None):
        """
        Inicializa el cifrador.
        Args:
            key (bytes, opcional): Una llave existente. Si no se da, se genera una nueva.
        """
        if key:
            self.key = key
        else:
            self.key = Fernet.generate_key()
            
        self.cipher = Fernet(self.key)

    def encriptar(self, texto_plano: str) -> bytes:
        """
        Encripta un texto.
        Args:
            texto_plano (str): El mensaje original.
        Returns:
            bytes: El mensaje encriptado (parece basura ilegible).
        """
        # Fernet necesita bytes, así que convertimos el string
        if not texto_plano:
            return b""
        
        datos_bytes = texto_plano.encode('utf-8')
        encriptado = self.cipher.encrypt(datos_bytes)
        return encriptado

    def desencriptar(self, texto_encriptado: bytes) -> str:
        """
        Desencripta un texto.
        Args:
            texto_encriptado (bytes): El mensaje cifrado.
        Returns:
            str: El mensaje original legible.
        """
        if not texto_encriptado:
            return ""
            
        decifrado_bytes = self.cipher.decrypt(texto_encriptado)
        return decifrado_bytes.decode('utf-8')

    def obtener_key(self) -> bytes:
        """Retorna la llave actual para que pueda ser guardada en un archivo .key"""
        return self.key