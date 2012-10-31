XBian 1.0 Alpha 1
=============================

How-to install
=============================
1. Download and restore the latest raspbian image to a SD-card.
2. Follow the instructions of the Setup.sh located in the Docs folder.
3. Enjoy!

Minor bugs
=============================
1. XBMC thumbnail aspect ratio wrong
2. XBMC still hangs occasionally

Missing features
=============================
1. XBOX remote to lirc (Tried but not working)
2. Implement xbian-config update function (CurlyMo will this implement after the release of Xbian 1.0 Alpha)
3. Implement xbian-config license setup - Done
4. Add licenses and author information to all (custom made) scripts - Done
5. Implement all wireless driver
6. Implement xbian-config hostname setup
7. PVR Addons
8. Drivers for PVR Backend
9. Implement all wireless drivers
10. Implement xbian-config hostname setup - Done
                                          - 
Needs testing
=============================
1. Test wireless with existing kernel modules (Seems to work)

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
5. Realtek 8192cu

xbian-config
=================================
1. Info<br />
2. Settings<br />
2.1. Resize SD<br />
2.2. Change password<br />
2.3. Set timezone<br />
2.4. SSH root login<br />
2.5. Overclocking<br />
2.6. License MPG2<br />
2.7. License VC-1<br />
2.8. Hostname<br />
3. Packages<br />
3.1. Remote<br />
3.1.1. Development<br />
3.1.2. Web<br />
3.2. Local<br />
4. Update<br />
