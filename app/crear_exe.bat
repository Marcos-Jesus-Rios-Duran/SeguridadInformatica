@echo off
echo Borrando versiones anteriores...
rmdir /s /q build
rmdir /s /q dist
del /q *.spec

echo Generando CriptoApp.exe...
:: Este comando crea el ejecutable en un solo archivo y sin consola negra
pyinstaller --name="CriptoApp" --windowed --onefile --clean --icon=NONE main.py

echo.
echo ==========================================
echo    PROCESO TERMINADO EXITOSAMENTE
echo ==========================================
pause