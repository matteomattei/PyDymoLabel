!define exe             'PyDymoLabel.exe'

!define compressor      'lzma'  ;one of 'zlib', 'bzip2', 'lzma'
!define icon            'chip2bit.ico'

; - - - - do not edit below this line, normaly - - - -
!ifdef compressor
    SetCompressor ${compressor}
!else
    SetCompress Off
!endif
Name ${exe}
OutFile ${exe}
SilentInstall silent
!ifdef icon
    Icon ${icon}
!endif

Section
	SetOutPath '$EXEDIR\PYDYMOLABEL-Portable'
	SetOverwrite on
	File /r build\exe.win32-3.4\*.*
	SetOutPath '$EXEDIR\'
	ExecWait "$EXEDIR\PYDYMOLABEL-Portable\PyDymoLabel.exe"
	RMDir /r '$EXEDIR\PYDYMOLABEL-Portable'
SectionEnd