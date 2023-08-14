@ECHO OFF
CD %~dp0
ECHO --------------------------------

SET Solution=MeowkitPy
SET Proj=MeowkitPy

SET PyVersion=3.9
SET PyDir="C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64"
SET PATH=%PyDir%;%PATH%

SET Root=%~dp0../%Solution%

SET Venv=env-meowkit-py%PyVersion%
SET VenvDir=%Root%/%env%/Scripts


SET python="%PyDir:~1,-1%\python.exe"
if not exist %python% (
    ECHO "Cannot find PATH of python.exe"
    exit /b 1
) else (
    ECHO "Found >> %python:~1,-1%"
    ECHO --------------------------------
)

