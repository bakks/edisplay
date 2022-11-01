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
