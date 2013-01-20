#This will reboot your Pi automatically after a few seconds if it crashes for any reason

sudo modprobe bcm2708_wdog
sudo vi /etc/modules

# Add the line "bcm2708_wdog"

sudo apt-get install watchdog
chkconfig watchdog on
sudo /etc/init.d/watchdog start
sudo vi /etc/watchdog.conf

# Uncomment the line watchdog-device = /dev/watchdog
