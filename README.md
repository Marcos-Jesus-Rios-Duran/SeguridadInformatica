# SeguridadInformatica
Este repositorio contiene practicas de la asignatura Seguridad Informática.
🔒
# 🐍 Guía: Entorno Virtual y PyQt6 en Windows

## 📋 Estructura del Proyecto
```
C:\dev\SeguridadInformatica\
├── enviromentapp/          # Entorno virtual
├── app/                    # Tu aplicación
│   ├── main.py            # Archivo principal
│   └── requirements.txt   # Dependencias
└── README.md
```

---

## 🚀 Configuración Inicial (Solo una vez)

### 1. Crear el entorno virtual
```bash
cd C:\dev\SeguridadInformatica
py -m venv enviromentapp
```

### 2. Activar el entorno virtual
```bash
enviromentapp\Scripts\activate
```
Deberías ver `(enviromentapp)` al inicio de la línea.

### 3. Actualizar pip
```bash
py -m pip install --upgrade pip
```

### 4. Crear `requirements.txt`
En la carpeta `app/`, crea el archivo `requirements.txt`:
```txt
PyQt6
cryptography
```

### 5. Instalar dependencias
```bash
cd app
py -m pip install -r requirements.txt
```

---

## 💻 Uso Diario

### Activar el entorno (cada vez que abras el CMD)
```bash
cd C:\dev\SeguridadInformatica
enviromentapp\Scripts\activate
```

### Ejecutar tu aplicación
```bash
cd app
py main.py
```

### Desactivar el entorno (cuando termines)
```bash
deactivate
```

---

## 🔧 Comandos Útiles

### Instalar un nuevo paquete
```bash
py -m pip install nombre_paquete
```

### Ver paquetes instalados
```bash
py -m pip list
```

### Actualizar requirements.txt
```bash
py -m pip freeze > requirements.txt
```

### Reinstalar todo desde cero
```bash
py -m pip install -r requirements.txt
```

---

## ❌ Solución de Problemas

### Error: "pip no se reconoce"
**Solución:** Usa siempre `py -m pip` en lugar de solo `pip`

### Error: "No module named PyQt6"
**Solución:** 
1. Verifica que el entorno esté activado (debe aparecer `(enviromentapp)`)
2. Reinstala: `py -m pip install PyQt6`

### Error: Microsoft Visual C++ requerido
**Solución:** No especifiques versiones exactas en `requirements.txt`
```txt
# ❌ Malo
PyQt6==6.7.1

# ✅ Bueno
PyQt6
```

### El entorno no se activa
**Solución:** Ejecuta:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Luego intenta activar de nuevo.

---

## 📦 Paquetes Instalados

Después de seguir esta guía tendrás:
- **PyQt6** (6.10.0+) - Framework para GUI
- **PyQt6-Qt6** - Bibliotecas Qt
- **PyQt6-sip** - Bindings Python-Qt
- **cryptography** (46.0.3+) - Cifrado y seguridad
- **cffi** - Foreign Function Interface
- **pycparser** - Parser de C

---

## 🎯 Ejemplo de Validación de Campos

```python
# ❌ Incorrecto
if not usuario & not password:
    QMessageBox.warning(self, "Error", "Campos vacios")

# ✅ Correcto
if not usuario or not password:
    QMessageBox.warning(self, "Error", "No se permiten campos vacíos")
    return False
```

---

## 📝 Notas Importantes

- Siempre usa `py` en lugar de `python` en Windows
- El entorno virtual debe activarse cada vez que abres una nueva terminal
- No subas la carpeta `enviromentapp/` a Git (agrégala a `.gitignore`)
- `requirements.txt` es suficiente para que otros recreen el entorno

---

## 🔄 Clonar el Proyecto en Otra PC

```bash
# 1. Clonar el repositorio
git clone tu-repositorio

# 2. Crear entorno virtual
cd SeguridadInformatica
py -m venv enviromentapp

# 3. Activar entorno
enviromentapp\Scripts\activate

# 4. Instalar dependencias
cd app
py -m pip install -r requirements.txt

# 5. Ejecutar
py main.py
```

---

## ✅ Checklist de Verificación

- [ ] Entorno virtual creado
- [ ] Entorno activado (ves `(enviromentapp)`)
- [ ] pip actualizado
- [ ] requirements.txt creado
- [ ] Dependencias instaladas
- [ ] Aplicación ejecutándose

---

**¡Listo! Tu entorno está configurado correctamente.** 🎉