#!/bin/bash
#
#Copyright 2012 CurlyMo, Erwin Bovendeur <development@xbian.org>
#Aron Robert Szabo <aron@reon.hu>
#Frank Buss <fb@frank-buss.de>
#
#This file is part of XBian - XBMC on the Raspberry Pi.
#
#XBian is free software: you can redistribute it and/or modify it under the 
#terms of the GNU General Public License as published by the Free Software 
#Foundation, either version 3 of the License, or (at your option) any later 
#version.
#
#XBian is distributed in the hope that it will be useful, but WITHOUT ANY 
#WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
#FOR A PARTICULAR PURPOSE. See the GNU General Public License for more 
#details.
#
#You should have received a copy of the GNU General Public License along 
#with XBian. If not, see <http://www.gnu.org/licenses/>
#

#Download compilation tools from the official raspberry pi github
cd /usr/src
sudo git clone --depth 5 https://github.com/raspberrypi/tools.git
cd tools
sudo ln -s /usr/src/tools/arm-bcm2708/arm-bcm2708-linux-gnueabi/bin/arm-bcm2708-linux-gnueabi-gcc /usr/bin/arm-bcm2708-linux-gnueabi-gcc

#Download the official kernel from the raspberry pi github
sudo mkdir /opt/raspberry
cd /opt/raspberry
sudo git clone --depth 5 git://github.com/raspberrypi/linux.git
mv linux linux3.2.27

#Begin 3.6.1
cp -R linux3.2.27 linux3.6.1
cd linux3.6.1/
git checkout rpi-3.6.y
cd /opt/raspberry
rm -r linux3.6.1/drivers/misc/vc04_services
cp -R linux3.2.27/drivers/misc/vc04_services linux3.6.1/drivers/misc/
rm -r linux3.6.1/sound/arm
cp -R linux3.2.27/sound/arm linux3.6.1/sound
rm -r linux3.6.1/drivers/staging/media/lirc
cp -R linux3.2.27/drivers/staging/media/lirc linux3.6.1/drivers/staging/media/
cd /opt/linux3.6.1
#End 3.6.1


#Begin 3.2.27
cd linux3.2.27
#End 3.2.27

#Begin 3.2.27
#Download the used config from the XBian github for 3.2.27
sudo wget https://raw.github.com/xbianonpi/xbian/master/Patches/kernel/.config3_2_27
mv .config3_2_27 .config
#End 3.2.27

#Begin 3.6.1
#Download the used config from the XBian github for 3.2.27
sudo wget https://raw.github.com/xbianonpi/xbian/master/Patches/kernel/.config3_6_1
mv .config3_6_1 .config
#End 3.6.1

#Symlink the lirc drivers to get the patch working
sudo wget https://raw.github.com/xbianonpi/xbian/master/Patches/kernel/additional-lirc_rpi+lirc_xbox.patch
sudo patch -p1 < additional-lirc_rpi+lirc_xbox.patch

#Stop XBMC to increase compilation speed
sudo kill -9 $(pgrep xbmc)

#Make steps with custom commands not supported by the official config
sudo make ARCH=arm CROSS_COMPILE=/usr/bin/ CONFIG_LIRC_STAGING=y CONFIG_LIRC_RPI=m CONFIG_I2C_DEV=m CONFIG_LIRC_RP1=m CONFIG_LIRC_XBOX=m CONFIG_DM_CRYPT=m
sudo make modules ARCH=arm CROSS_COMPILE=/usr/bin/ CONFIG_LIRC_STAGING=y CONFIG_LIRC_RPI=m CONFIG_I2C_DEV=m CONFIG_LIRC_RP1=m CONFIG_LIRC_XBOX=m CONFIG_DM_CRYPT=m
sudo make modules_install ARCH=arm CROSS_COMPILE=/usr/bin/ CONFIG_LIRC_STAGING=y CONFIG_LIRC_RPI=m CONFIG_I2C_DEV=m CONFIG_LIRC_RP1=m CONFIG_LIRC_XBOX=m CONFIG_DM_CRYPT=m INSTALL_MOD_PATH=/

#Implement the new kernel
cp arch/arm/boot/Image /boot/kernel.img

#Reboot
reboot