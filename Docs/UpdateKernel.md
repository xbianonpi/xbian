\# This script will update your XBMC build to the latest one available on our GitHub<br />
<br />
\# Make a backup of the current kernel<br />
sudo cp /boot/kernel.img /boot/kernel.img.old
<br />
\# Cloning XBian GitHub<br />
sudo rm -rf /home/xbian/source<br />
cd /home/xbian/<br />
git clone --depth 5 https://github.com/Koenkk/xbian.git source<br />
cd source<br />
<br />
\# Installing the new kernel<br />
sudo cp -R lib/modules/3.6.1 /lib/modules/<br />
sudo cp boot/kernel3_6_1.img /boot/kernel.img<br />
sudo reboot<br />
<br />
\#Restoring the old kernel<br />
sudo mv /boot/kernel.img /boot/kernel.img.new<br />
sudo mv /boot/kernel.img.old /boot/kernel.img<br />
