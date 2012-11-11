[Preview] XBian 1.0 Alpha 2 Changelog
==================================
XBian 1.0 Alpha 2 mostly contains bugfixes that were
apparent in Alpha 1.0. Besides these bugfixes it also
contains some new features and improvements.

Bugfixes
==================================
- Issues #8 and #36: The keyboard and remotes that weren't working
- Issue #23: XBMC Library not updated.
- Issue #37: Airplay/zeroconf not working
- Issue #2: Video forward/backward freezes
- Issue #41: SSH not working
- Issues #52, #49: USB devices not visible

Improvements
==================================
- LIRC xbox module
- Kernel 3.6.1
- New XBMC nightly version
- PVR Addons
- Reduction of image size
- Resize SD card on first boot
- Autologin as xbian instead of root user
- Modular xbian-config

Xbian-config additions
==================================
- Ability to switch kernel version
- Change various video hardware settings
- Added Samba package
- Fixes cross dependent packages

XBian 1.0 Alpha 1 Changelog
==================================
XBian 1.0 Alpha 1 is a fresh start. One of the biggest changes
is that we are now using GitHub. GitHub allows us to make XBian
100% open to everyone. We hope this motivates people to help
us with developing XBian.

NOTE: If you are connecting via SSH use user:xbian pass:raspberry

GPL 3.0 Licenses
=================================
XBian has adopted the GPL 3.0 licenses on all it's code.
So we're completely open source.

New XBian basis
=================================
XBian 1.0 is build from scratch from the latest Raspbian (28-10)
version. This fixes a lot of issues that were present on the
previous XBian versions.

XBian Config
=================================
XBian config allows users to setup their XBian installation
very easily. Currently it's allows you to set the following
settings:

- Resize SD: This option resizes your root partition to take
  full advantage of the space available on your SD card. It
  will also make a swap partition based on the size of your
  SD card.
- Change password: This allows you to change the password
  of the default user and root user (the default user is xbian).
- Set timezone: This allows you to change the timezone of
  the system.
- SSH root login: Enable/disable root login through SSH
- Overclocking: This option allows you to set different over
  clocking options. We recommend using the default XBian
  overclock because this is a very stable over clock. If you
  want more performance you can set a higher over clock. Keep
  in mind that we are NOT responsible for any damage caused
  to your raspberry pi.
- License MPG2/VC-1: This option allows you to easily set
  your MPG2 and VC-1 license keys.
- Hostname: You can easily change the hostname of you pi.
- Configure LAN: Enables static of DHCP configuration
  of your wired network connection.
- Configure WLAN: Enables static of DHCP configuration
  of your wireless network connection. Also gives options
  to enter you're SSID and password.

We also added a 'extra package' option. This allows you to
easily install extra packages, for example: web server.
We will also introduce a update system once XBian 1.0
hits final.

You can easily access xbian-config by ssh'ing into your pi (user:xbian pass:raspberry). 

Kernel
==============================
This XBian is build with a custom kernel. We've added
some custom modules:
- lirc_rpi
- i2c*
- w1*
- spi*

These modules will allow developers to add and control
additional electronics through the GPIO pins.

Another improvement is that we're using "performance"
as the default governor. This will make all supported
overclocking static without voiding you're warranty.
The difference with force_turbo=1 is that kernel
doesn't directly control the voltage level.

Other improvements & features
==============================
- Blocked the root ssh login for security reasons.
- Improved USB mounting
- Improved boot time
- Improved the startup process by using init scripts.
- Finally got rid of all the command line text
  appearing behind XBMC user interface.
- Running XBMC as xbian user
- Added a LOT of wireless drivers.
- Improved performance of XBMC

Special thanks to
==============================
Hexagon and deHakkelaar


Final note by Koenkk
==============================
As you might have already noticed a new main developper
appeared in our team, his name is CurlyMo. I really
really really want to thank him a LOT! He did a very
big part of the development of XBian 1.0. We couldn't
have done this without him!