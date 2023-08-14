@ECHO OFF

SET solution=MeowkitPy
SET proj_name=meowkit
SET ver_python=3.9

SET root=%~dp0../%solution%
SET env=env-%proj_name%-py%ver_python%
SET path=%~dp0../%solution%/%env%/Scripts


SET setup=%~dp0../%solution%/setup.py

if exist %path%/python.exe (
    ECHO "Found >> %env%"

    REM Update Version
    %path%/python.exe package.py
    for /f "usebackq delims=" %%i in ("%file_path%") do (
        SET "version=%%i"
    )
    ECHO %version%

    CD %root%
    REM %path%/python.exe %setup% bdist_wheel --dist-dir %~dp0
    %path%/python.exe -m build --outdir %~dp0/Package

) else (
    ECHO "Cannot found the env << %path%"
)

pause