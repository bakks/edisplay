#!/bin/bash
set -e

#OUTPUT=$(./fetch | tail -1)
d=$(TZ='America/Los_Angeles' date +'%Y/%m/%d')
#rm -f nytimes.bmp
rm -f scan.pdf nytimes.bmp
#wget https://static01.nyt.com/images/${d}/nytfrontpage/scan.pdf
#convert -density 200 scan.pdf -crop 2360x4310+40+190 -resize x1872 -rotate 270 nytimes.bmp
convert -density 200 scan.pdf -crop 2360x3700+40+190 -resize x1872 -rotate 270 nytimes.bmp
./display -1.14 nytimes.bmp

