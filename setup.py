import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
	base = "Win32GUI"

executableOptions = [
	Executable(
		"PyDymoLabel.py",
		appendScriptToExe=True,
		appendScriptToLibrary=False,
		targetName="PyDymoLabel.exe",
		base = base # <-- this is needed to hide Windows console
	)
]

buildOptions = dict(
	compressed=True,
	create_shared_zip = False,
	excludes = [],
	packages = [],
	include_files = ['my.label'],
)

setup(
	name = "PyDymoLabel",
	version = '1.0',
	description = "A simple tool to print labels with Dymo printers",
	author = 'Matteo Mattei',
	author_email = 'matteo.mattei@gmail.com',
	options = dict(build_exe = buildOptions),
	executables = executableOptions
)