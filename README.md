You can download a fresh XBian 1.0 Alpha 3 image from here: http://jb.xenserver.sk/xbian/XBian1.0Alpha3.7z

#XBian 1.0 Alpha 3 Changelog
==================================
XBian 1.0 Alpha 3 contains some new important features. 
We've set-up a custom apt repository for installing updates 
and packages. Updating XBian is now as easy as updating 
debian packages. Just run apt-get upgrade. We've also added
the first beta of XBMC v12 - Frodo. So, XBMC will be a
lot more stable in Alpha 3.

##Introduction to our xbian apt repository
==================================
We've set up our own apt repository. This enables us to update
the system with apt-get upgrade. However, a cool new feature is
that you don't have to wait until a new update is released to
update individual XBian packages. We shall release new versions
of the kernel, XBMC, Lirc and xbian-config seperately from the
XBian updates. When you install the final update, XBian will
know what version of a certain program you're running so you 
don't have to reinstall it again. The final update will then
only contain some minor patches to core system files. However,
it could happen that we have to hold some packages back because
of some work in progress from our side. But most of the time
you can just update the packages in between official releases.

##Bugfixes
==================================
- Issue #63: [xbian-config] No reboot after network change
- Issue #70: XBMC couldn't access the USB attached drive
- Issue #72: Black terminal when exiting XBMC
- Issue #93: [xbian-config] Static network configuration doesn't work
- Issue #101: [xbian-config] Incorrect flag names in videoflags module
- Issue #106: Library update hangs the raspberry pi halfway over SMB share (fixed by issue #74)

##Improvements
==================================
- Issue #38: Start xbian-config when exiting XBMC
- Issue #74 and #75: Upgraded to XBMC v12 - Frodo Beta 1
- Issue #88: Advancedsettings.xml is now XBMC v12 - Frodo proof
- Issue #92: MythTV PVR add-on
- Issue #66: XBian apt repository 
- Issue #76: LIRC srm7500libusb support
- Issue #91: ASS subtitle support
- Issue #93 and #58: [xbian-config] Network settings fully functional
- Issue #84: Improved memory split
- Issue #98: Libcec 2.0.4: [Changelog here](https://github.com/Pulse-Eight/libcec/blob/master/ChangeLog)
- Issue #96: Kernel 3.6.7

##XBian-config additions
==================================
- Issue #57 and #34: Removed dependency of LUA
- Issue #93 and #58: Fixed network settings
- Issue #73: New section for managing installed services
- Issue #61: Fixed button labels for Root enabled SSH ()
- Issue #66 and #62: Add/remove packages + updates through apt repository 

##Special thanks to
==============================
Firesphere, BartOtten, deHakkelaar, Brantje