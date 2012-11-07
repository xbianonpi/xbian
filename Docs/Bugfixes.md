Bugfixes for XBian 1.0 Alpha 1
======================================================
- Bug #8 Keyboard not working, fix: sudo usermod -a -G input xbian
- Bug #27 Unable to add a library source by NFS, fix: https://github.com/Koenkk/xbian/issues/29
- Fixed an issue where the logitech K400 keyboard did not always work. People say it's due to the 3.2.27 kernel and should be fixed in 3.6.x (unconfirmed). 
  The issue seems to be fixed by adding the following lines to /etc/rc.local before exit 0;<br />
modprobe -r hid_logitech_dj<br />
modprobe hid_logitech_dj<br />