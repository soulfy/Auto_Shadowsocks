@echo off
:cd /d %~dp0\allServer
set base=%~dp0\allServer

rem ѡ��ѡ��
echo ----------------------1. Japan��A������----------------------
echo.
echo ----------------------2. Japan-B-Server----------------------
echo.
echo ----------------------3. Japan-C-Server----------------------
echo.
echo ----------------------4. Singapore-A-Server----------------------
echo.
echo ----------------------5. Singapore-B-Server----------------------
echo.
echo ----------------------6. Singapore-C-Server----------------------
echo.
echo ----------------------7. Usa-A-Server----------------------
echo.
CHOICE /C 1234567 /M Please--Input--the--Server--Num

python %base%\api_shadowsocks.py %errorlevel%

:end
pause
