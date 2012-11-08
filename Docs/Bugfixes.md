Bugfixes for XBian 1.0 Alpha 1
======================================================
- Issue #36 Keyboard not working, fix: sudo sed -i '$d' /etc/rc.local && sudo echo -e "chmod 0777 /dev/tty0\nexit 0" >> /etc/rc.local
- Issue #37 Airplay/Zeroconf is not working in XBian 1.0 Alpha 1, fix: sudo apt-get install avahi-daemon
- Issue #23 Movies/TvShows not being added to Libraries, fix: adding a new XBMC build.
- Issue #8 Keyboard not working, fix: sudo usermod -a -G input xbian
- Issue #27 Unable to add a library source by NFS, fix: https://github.com/Koenkk/xbian/issues/29
- Fixed an issue where the logitech K400 keyboard did not always work. People say it's due to the 3.2.27 kernel and should be fixed in 3.6.x (unconfirmed). 
  The issue seems to be fixed by adding the following lines to /etc/rc.local before exit 0;<br />
modprobe -r hid_logitech_dj<br />
modprobe hid_logitech_dj<br />
