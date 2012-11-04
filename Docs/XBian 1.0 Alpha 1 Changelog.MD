XBian 1.0 Alpha 1 Changelog
==================================
XBian 1.0 Alpha 1 is a fresh start. One of the biggest changes is that we are now using GitHub. GitHub allows us to make XBian 100% open for everyone. We hope this motivates people to help us with developing XBian. 

XBian Config
=================================
XBian config allows users to setup their XBian installation very easily. Currently its allows you to set the following settings:
- Resize SD: This option resizes your root partition to take full advantage of the space available on your SD card. It will also make a swap partition based on the size of your SD card. 
- Change password: This allows you to change the password of the default user (the default user is xbian).
- Set timezone: This allows you to change the timezone of the system.
- Overclocking: This option allows you to set different over clocking options. We recommend using the default XBian overclock because this is a very stable over clock. If you want more performance you can set a higher over clock. Keep in mind that we are NOT responsible for any damage caused to your raspberry pi. 
- License MPG2/VC-1: This option allows you to easily set your MPG2 and VC-1 license keys.
- Hostname: You can easily change the hostname of your raspberry pi. 

We also added a 'extra package' option. This allows you to easily install extra packages, for example: web server. We will also introduce a update system once XBian 1.0 hits final.

Other improvements & features
==============================
- Blocked the root ssh login for security reasons.
- Improved USB mounting
- Improved boot time
- Improved the startup process by using init scripts.
- Finally got rid of all the command line text appearing behind XBMC user interface.
- Updated the kernel & firmware
- Added lirc gpio module
- Added a LOT of wireless drivers.
- Improved performance of XBMC


