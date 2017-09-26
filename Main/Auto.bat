@echo off

cd allServer
rem 选择选项
echo ----------------------1. Japan的A服务器----------------------
echo.
echo ----------------------2. Japan的B服务器----------------------
echo.
echo ----------------------3. Japan的C服务器----------------------
echo.
echo ----------------------4. Singapore的A服务器----------------------
echo.
echo ----------------------5. Singapore的B服务器----------------------
echo.
echo ----------------------6. Singapore的C服务器----------------------
echo.
echo ----------------------7. Usa的A服务器----------------------
echo.
CHOICE /C 1234567 /M 请选择你要使用的服务器

if %errorlevel%==1 goto JapanA
if %errorlevel%==2 goto JapanB
if %errorlevel%==3 goto JapanC
if %errorlevel%==4 goto SingaporeA
if %errorlevel%==5 goto SingaporeB
if %errorlevel%==6 goto SingaporeC
if %errorlevel%==7 goto UsaA

:JapanA
Japan_A_shadowsocks.py
goto end

:JapanB
Japan_B_shadowsocks.py
goto end

:JapanC
Japan_C_shadowsocks.py
goto end

:SingaporeA
Singapore_A_shadowsocks.py
goto end

:SingaporeB
Singapore_B_shadowsocks.py
goto end

:SingaporeC
Singapore_C_shadowsocks.py
goto end

:UsaA
USA_A_shadowsocks.py
goto end

:end
pause
