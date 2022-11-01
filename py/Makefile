console:
	screen /dev/tty.usbmodem14401 115200

copy: lib/neopixel.mpy
	cp code.py /Volumes/CIRCUITPY/
	rsync -r lib/* /Volumes/CIRCUITPY/lib/

dev:
	find . -name "*.py" | entr -c make copy

https://downloads.circuitpython.org/bin/adafruit_macropad_rp2040/en_US/adafruit-circuitpython-adafruit_macropad_rp2040-en_US-7.3.3.uf2
circuitpy_exact_version = 7.3.3
circuitpy_uf2 = adafruit-circuitpython-adafruit_macropad_rp2040-en_US-$(circuitpy_exact_version).uf2
circuitpy_version = 7.x
circuitpy_release = 20221101
circuitpy_filename = adafruit-circuitpython-bundle-${circuitpy_version}-mpy-${circuitpy_release}
tmp = /var/tmp
makefile_dir = $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

py_libs = adafruit_debouncer.mpy adafruit_macropad.mpy adafruit_pixelbuf.mpy adafruit_simple_text_display.mpy adafruit_ticks.mpy neopixel.mpy adafruit_hid adafruit_bitmap_font adafruit_display_text

reinstall_circuitpy:
	cd $(tmp) && wget https://downloads.circuitpython.org/bin/adafruit_macropad_rp2040/en_US/$(circuitpy_uf2)
	echo "double click the button on the left of the macropad now!!!"
	sleep 10
	cd $(tmp) && cp $(circuitpy_uf2) /Volumes/RPI-RP2

lib/neopixel.mpy: $(tmp)/$(circuitpy_filename)
	cd $(tmp)/$(circuitpy_filename)/lib && cp -r $(py_libs) $(makefile_dir)/lib/

$(tmp)/${circuitpy_filename}.zip:
	cd $(tmp) && wget https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/$(circuitpy_release)/${circuitpy_filename}.zip

$(tmp)/$(circuitpy_filename): $(tmp)/$(circuitpy_filename).zip
	cd $(tmp) && unzip $(circuitpy_filename).zip

clean_lib:
	rm -r ./lib/*
	rm -rf /Volumes/CIRCUITPY/lib/*


