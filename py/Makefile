console:
	screen /dev/tty.usbmodem14401 115200

copy:
	cp code.py /Volumes/CIRCUITPY/
	cp lib/* /Volumes/CIRCUITPY/lib/

dev:
	find . -name "*.py" | entr -c make copy
