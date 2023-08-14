@ECHO OFF



CALL %~dp0env.bat
if errorlevel 1 ( exit 1 )

REM Update Version
%python% package.py 0 0 1
for /f "usebackq delims=" %%i in ("version.txt") do (
    SET "version=%%i"
)
REM ECHO [DEBUG]: %version%


if not exist %~dp0Package ( md %~dp0Package )
if not exist %~dp0Package\Cache ( md %~dp0Package\Cache )

REM 緩存舊版本
for %%i in (%~dp0Package\*.gz %~dp0Package\*.whl) do (
    move "%%i" "%~dp0Package\Cache"
    ECHO "Move: %%i"
)

CD %Root%
ECHO "Starting Packaging"
REM %python% -m build --outdir %~dp0/Package

REM SET setup=%~dp0../%Solution%/setup.py
REM %python% %setup% bdist_wheel --dist-dir %~dp0

ECHO --------------------------------
ECHO Done
ECHO.