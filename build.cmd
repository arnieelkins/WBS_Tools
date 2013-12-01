@echo off
del /q dist
rmdir /s /q dist build
python -OO setup.py py2exe --bundle 1
copy c:\python27\lib\site-packages\wx-2.8-msw-unicode\wx\gdiplus.dll dist
copy C:\SkyDrive\python\win_todist\msvcr90.dll dist
copy C:\SkyDrive\python\win_todist\msvcm90.dll dist
copy C:\SkyDrive\python\win_todist\msvcp90.dll dist
copy C:\SkyDrive\python\win_todist\Microsoft.VC90.CRT.manifest dist
del /q dist\w9xpopen.exe