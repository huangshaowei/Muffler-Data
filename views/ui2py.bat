@echo on
setlocal enabledelayedexpansion
set UI2PY="E:\Binary\FreeCAD_trunk\bin\Python27\Lib\site-packages\PyQt4\pyuic4.bat"
for %%i in (*.ui) do (
set p=%%i
set fn=%CD%\!p:~0,-2!py
call %UI2PY% %CD%\%%i > !fn!
)
