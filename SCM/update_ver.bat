@ECHO OFF

SET solution=MeowkitPy
SET proj_name=meowkit
SET ver_python=3.9

SET root=%~dp0../%solution%
SET env=env-%proj_name%-py%ver_python%
SET path=%~dp0../%solution%/%env%/Scripts

cd %path%

python %~dp0package.py

pause