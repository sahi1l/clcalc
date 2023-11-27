mac: CLCalc.py CLCalc.icns
	pyinstaller --windowed --onefile CLCalc.py
	. ./setIcon.sh CLCalc.icns dist/CLCalc.app
