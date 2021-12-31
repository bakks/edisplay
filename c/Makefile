DIR_Config   = ./lib/Config
DIR_EPD      = ./lib/e-Paper
DIR_FONTS    = ./lib/Fonts
DIR_GUI      = ./lib/GUI
DIR_Examples = ./examples

DIR_BIN      = ./bin

OBJ_C = $(wildcard ${DIR_Config}/*.c ${DIR_EPD}/*.c ${DIR_FONTS}/*.c ${DIR_GUI}/*.c ${DIR_Examples}/*.c )
OBJ_O = $(patsubst %.c,${DIR_BIN}/%.o,$(notdir ${OBJ_C}))

TARGET = epd

CC = gcc

MSG = -g -O0 -Wall
DEBUG = -D USE_DEBUG
STD = -std=gnu99

CFLAGS += $(MSG) $(DEBUG) $(STD)

LIB = -lbcm2835 -lm -lrt -lpthread
ext_bin = IT8951-ePaper/Raspberry/bin/

$(shell mkdir -p $(DIR_BIN))

../bin/display:main.o
	$(CC) $(CFLAGS) main.o $(ext_bin)/GUI_BMPfile.o $(ext_bin)/DEV_Config.o $(ext_bin)/EPD_IT8951.o $(ext_bin)/GUI_Paint.o $(ext_bin)/font24.o $(LIB) -o ../bin/display

main.o:main.c IT8951-ePaper/Raspberry/bin/GUI_BMPfile.o
	$(CC) $(CFLAGS) main.c -c -o main.o

IT8951-ePaper/Raspberry/lib/GUI/GUI_BMPfile.c:
	git clone https://github.com/waveshare/IT8951-ePaper.git

IT8951-ePaper/Raspberry/bin/GUI_BMPfile.o: IT8951-ePaper/Raspberry/lib/GUI/GUI_BMPfile.c
	cd IT8951-ePaper/Raspberry && make


clean :
	rm ../bin/display
	rm main.o
	rm IT8951-ePaper/Raspberry/bin/*.o

