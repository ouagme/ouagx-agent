@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (echo Python 3.11+ is required.&pause&exit /b 1)
if not exist ".venv\Scripts\python.exe" py -m venv .venv
call ".venv\Scripts\activate.bat"
if not exist ".venv\.ouagx_deps_installed" (python -m pip install --upgrade pip & python -m pip install -r requirements.txt & type nul > ".venv\.ouagx_deps_installed")
if not exist ".env" copy ".env.example" ".env" >nul
python -m ouagx_agent
endlocal
