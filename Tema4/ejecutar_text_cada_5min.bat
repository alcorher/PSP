@echo off
echo Iniciando ejecución de text.py cada 5 minutos...

:loop
python test.py
echo Esperando 5 minutos...
timeout /t 300 /nobreak > nul
goto loop
