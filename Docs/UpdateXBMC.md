# This script will update your XBMC build to the latest one available on our GitHub

# Stopping XBMC and making a backup of the current XBMC
sudo /etc/init.d/xbmc stop
sudo mv /usr/local/lib/xbmc /usr/local/lib/xbmc.bak
sudo mv /usr/local/share/xbmc /usr/local/share/xbmc.bak


# Cloning XBian GitHub
sudo rm -rf /home/xbian/source
cd /home/xbian/
git clone --depth 5 https://github.com/Koenkk/xbian.git source
cd source

# Installing the new XBMC build
sudo cp -R /usr/local/lib/xbmc /usr/local/lib
sudo cp -R /usr/local/share/xbmc /usr/local/share
sudo chmod +x /usr/local/lib/xbmc/xbmc.bin

# Starting the new XBMC build
sudo /etc/init.d/xbmc start



# If you want to restore to the old XBMC build execute the following commands
sudo /etc/init.d/xbmc stop
sudo rm -rf /usr/local/lib/xbmc
sudo rm -rf /usr/local/share/xbmc
sudo mv /usr/local/lib/xbmc.bak /usr/local/lib/xbmc
sudo mv /usr/local/share/xbmc.bak /usr/local/share/xbmc
sudo /etc/init.d/xbmc start