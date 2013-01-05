\# This script will update your XBMC build to the latest one available on our GitHub<br />
<br />
\# Stopping XBMC and making a backup of the current XBMC<br />
sudo /etc/init.d/xbmc stop<br />
sudo mv /usr/local/lib/xbmc /usr/local/lib/xbmc.bak<br />
<br />
\# Cloning XBian GitHub<br />
sudo rm -rf /home/xbian/source<br />
cd /home/xbian/<br />
git clone --depth 5 -b xbian-alpha5 https://github.com/xbianonpi/xbian.git source<br />
cd source<br />
<br />
\# Installing the new XBMC build<br />
sudo cp -R usr/local/lib/xbmc /usr/local/lib<br />
sudo cp -R usr/local/share/xbmc /usr/local/share<br />
sudo chmod +x /usr/local/lib/xbmc/xbmc.bin<br />
<br />
\# Starting the new XBMC build<br />
sudo /etc/init.d/xbmc start<br />
<br />
\# If you want to restore to the old XBMC build execute the following commands<br />
sudo /etc/init.d/xbmc stop<br />
sudo rm -rf /usr/local/lib/xbmc<br />
sudo mv /usr/local/lib/xbmc.bak /usr/local/lib/xbmc<br />
sudo /etc/init.d/xbmc start<br />
