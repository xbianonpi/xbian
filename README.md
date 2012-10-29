XBian 1.0 Alpha 1
=============================

How-to install
=============================
1. Download and restore the latest raspbian image to a SD-card.
2. Follow the insturctions of the Setup.sh located in the Docs folder.
3. Enjoy!

Minor bugs
=============================
1. XBMC thumbnail aspect ratio wrong
2. XBMC still hangs occasionally

Missing features
=============================
1. XBOX remote to lirc
2. Implement xbian-config update function
3. Implement xbian-config license setup
4. Add licenses and author information to all (custom made) scripts

Needs testing
=============================
1. Test wireless with existing kernel modules

Major steps
=============================
1. Install Raspbian - Done
2. Install CurlyMo kernel similar to r-win kernel v3. - Done
3. Move XBMC build from Xbian to new install. Done
4. Remove/Add packages - Done
5. Add xbian user (optional) - Done
6. Add init scripts - Done
7. Add recompiled lirc - Done
8. Add wiringPi (as additional module)
9. Patch raspi-config --> create xbian-config
10. Resize partition on boot and create a swap partition depending on SD card size - Done

Kernel 3.2.27 - Additional modules
=================================
1. lirc_rpi
2. i2c*
3. w1*
4. spi*

