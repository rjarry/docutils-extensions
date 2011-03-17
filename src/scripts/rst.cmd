@echo off
set SCRIPTS_FOLDER=%~dp0
set PYTHON_HOME=%SCRIPTS_FOLDER%\..

%PYTHON_HOME%\python "%SCRIPTS_FOLDER%\rst.py" %*
