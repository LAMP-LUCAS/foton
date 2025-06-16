@echo off
REM make-file.bat
REM Uso: make-file.bat [comando]

set COMMAND=%1
powershell -ExecutionPolicy Bypass -File make-file.ps1 %COMMAND%
