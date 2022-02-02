rem del /q dist
date /t
time /t
rmdir /s /q dist build

python -OO setup.py py2exe --bundle 1

xcopy /s icons\*.* dist\icons\
copy c:\python27\lib\site-packages\wx-2.8-msw-unicode\wx\gdiplus.dll dist
rem copy ..\wbs_includes\msvcr90.dll dist
rem copy ..\wbs_includes\msvcm90.dll dist
rem copy ..\wbs_includes\msvcp90.dll dist
rem copy ..\wbs_includes\Microsoft.VC90.CRT.manifest dist
del /q dist\w9xpopen.exe
date /t
time /t
