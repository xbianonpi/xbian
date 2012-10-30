#!/bin/bash

#Download compilation tools from the official raspberry pi github
cd /usr/src
sudo git clone --depth 5 https://github.com/raspberrypi/tools.git
cd tools
#Revert to the version used when building the kernel to ensure success
sudo git checkout 9c3d7b6ac692498dd36fec2872e0b55f910baac1
sudo ln -s /usr/src/tools/arm-bcm2708/arm-bcm2708-linux-gnueabi/bin/arm-bcm2708-linux-gnueabi-gcc /usr/bin/arm-bcm2708-linux-gnueabi-gcc

#Download the official kernel from the raspberry pi github
sudo mkdir /opt/raspberry
cd /opt/raspberry
sudo git clone --depth 5 git://github.com/raspberrypi/linux.git
cd linux
#Revert tot the version used when building the kernel to ensure success
sudo git checkout 10182a3bc434b27740f81c2b836a1af943060241

#Download the used config from the Xbian github
sudo wget https://raw.github.com/Koenkk/xbian/master/Patches/kernel/.config

#Symlink the lirc drivers to get the patch working
sudo ln -s /opt/raspberry/linux/drivers/staging/media/lirc /opt/raspberry/linux/drivers/staging/lirc
sudo wget https://raw.github.com/Koenkk/xbian/master/Patches/kernel/kernel.lirc_rpi-0.2.patch
sudo patch -p1 < kernel.lirc_rpi-0.2.patch

#Stop XBMC to increase compilation speed
sudo kill -9 $(pgrep xbmc)

#Make steps with custom commands not supported by the official config
sudo make CROSS_COMPILE=/usr/bin/ CONFIG_LIRC_STAGING=y CONFIG_LIRC_RPI=m CONFIG_I2C_DEV=m
sudo make modules CROSS_COMPILE=/usr/bin/ CONFIG_LIRC_STAGING=y CONFIG_LIRC_RPI=m CONFIG_I2C_DEV=m
sudo make modules_install CROSS_COMPILE=/usr/bin/ CONFIG_LIRC_STAGING=y CONFIG_LIRC_RPI=m CONFIG_I2C_DEV=m INSTALL_MOD_PATH=/

#Implement the new kernel
cp arch/arm/boot/Image /boot/kernel.img

#Build custom 8192co module
#Follow this guide:
#http://www.raspberrypi.org/phpBB3/viewtopic.php?f=53&t=11162

#Reboot
reboot
