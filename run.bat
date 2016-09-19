rmdir build /s /q
rmdir PYDYMOLABEL-Portable /s /q
del /s /q PyDymoLabel.exe
C:\Python34\python.exe setup.py build
"C:\Program Files (x86)\NSIS\makensis.exe" compile.nsi
pause
