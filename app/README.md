# 🔐 Sistema de Encriptación - App de Seguridad Informática

Aplicación de escritorio desarrollada con PyQt6 para encriptar y desencriptar mensajes de forma segura.

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone 
cd app_clase/app
```

### 2. Crear entorno virtual

**Windows:**
```bash
python -m venv enviromentapp
instalardependencias py -m ensurepip --default-pip
py -m pip --version
 en caso de que pip no seencuentre.
```

**Linux/Mac:**
```bash
python3 -m venv enviromentapp
```

### 3. Activar entorno virtual

**Windows:**
```bash
enviromentapp\Scripts\activate
```

**Linux/Mac:**
```bash
source enviromentapp/bin/activate
```

### 4. Instalar dependencias
```bash
pip install PyQt6
pip install cryptography
```

O si tienes un archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

## 🎨 Generar interfaces desde Qt Designer

Si modificas los archivos `.ui` en Qt Designer, necesitas regenerar los archivos Python:

### Generar todas las interfaces:
```bash
py -m PyQt6.uic.pyuic -x login.ui -o login.py
py -m PyQt6.uic.pyuic -x frnMenu.ui -o frnMenu.py
py -m PyQt6.uic.pyuic -x frnEncriptar.ui -o frnEncriptar.py
py -m PyQt6.uic.pyuic -x frnDesencriptar.ui -o frnDesencriptar.py
```

### Generar interfaz individual:
```bash
py -m PyQt6.uic.pyuic -x <archivo.ui> -o <archivo.py>
```

**Ejemplo:**
```bash
py -m PyQt6.uic.pyuic -x login.ui -o login.py
```

## ▶️ Ejecutar la aplicación

Con el entorno virtual activado:
```bash
python main.py
```

O:
```bash
py main.py
```

## 👤 Credenciales de Prueba

**Usuario:** `admin` o `Marcos`  
**Contraseña:** `mrco`

## 🛠️ Comandos Útiles

### Desactivar entorno virtual
```bash
deactivate
```

### Actualizar pip
```bash
python -m pip install --upgrade pip
```

### Generar requirements.txt
```bash
pip freeze > requirements.txt
```

### Limpiar caché de Python

**Windows:**
```bash
del /s /q __pycache__
del /s /q *.pyc
```

**Linux/Mac:**
```bash
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete
```

## 📦 Crear ejecutable (opcional)

### Instalar PyInstaller
```bash
pip install pyinstaller
```

### Generar ejecutable
```bash
pyinstaller --onefile --windowed --name "SistemaEncriptacion" main.py
```

El ejecutable se generará en la carpeta `dist/`

## 🔧 Desarrollo

### Workflow recomendado:

1. Diseñar interfaz en **Qt Designer** (genera `.ui`)
2. Convertir `.ui` a `.py` con el comando `pyuic`
3. Crear archivo `*BackEnd.py` con la lógica
4. Importar y usar en otros módulos

### Ejemplo:
```bash
# 1. Crear diseño en Qt Designer -> guardas como miVentana.ui
# 2. Convertir a Python
py -m PyQt6.uic.pyuic -x miVentana.ui -o miVentana.py
# 3. Crear miVentanaBackEnd.py con la lógica
# 4. Usar en tu aplicación
```

## ⚠️ Notas Importantes

- **NO** subir la carpeta `enviromentapp/` a Git (ya está en `.gitignore`)
- **NO** editar manualmente los archivos `.py` generados desde `.ui`
- Toda la lógica debe ir en los archivos `*BackEnd.py`
- Los archivos `.ui` son los archivos fuente, mantenerlos actualizados

## 📝 .gitignore recomendado
```gitignore
# Entorno virtual
enviromentapp/
venv/
env/
ENV/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
*.pyo
*.pyd
pip-log.txt
pip-delete-this-directory.txt

# PyQt
*.qmlc
*.jsc
*.ui.autosave

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Sistema Operativo
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
desktop.ini

# Archivos temporales
*.tmp
*.temp
*.log

# Distribución / Empaquetado
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
*.manifest
*.spec
```

## 📄 requirements.txt
```txt
PyQt6==6.7.1
PyQt6-Qt6==6.7.3
PyQt6-sip==13.8.0
cryptography==43.0.1
```

## 🤝 Contribuir

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es parte de un ejercicio académico de Seguridad Informática.

## 👨‍💻 Autor

**Marcos**  
Proyecto de clase - Seguridad Informática

---

💡 **Tip:** Siempre activa el entorno virtual antes de trabajar en el proyecto