# Epaper Display Project

## Setup

Raspberry Pi E-paper controller setup

```
sudo apt-get update
sudo apt-get install golang imagemagick libmagickwand-dev

sudo sed -i '/PDF/d' /etc/ImageMagick-6/policy.xml

cd ~                  
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.71.tar.gz                       
tar xvfz bcm2835-1.71.tar.gz;                      
cd bcm2835-1.71;                       
./configure;                      
make;        
sudo make install
```

cron
```
1 * * * * cd /var/tmp && /home/pi/edisplay/bin/run.sh
```

## Hardware

[Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)

[10.3inch e-Paper e-Ink Display HAT For Raspberry Pi](https://www.waveshare.com/product/displays/e-paper/epaper-1/10.3inch-e-paper-hat.htm)

[Adafruit MacroPad RP2040](https://learn.adafruit.com/adafruit-macropad-rp2040)
