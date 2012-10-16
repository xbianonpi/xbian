#!/bin/bash

cd /usr/src
sudo git clone https://github.com/raspberrypi/tools.git
sudo ln -s /usr/src/tools/arm-bcm2708/arm-bcm2708-linux-gnueabi/bin/arm-bcm2708-linux-gnueabi-gcc /usr/bin/arm-bcm2708-linux-gnueabi-gcc

sudo mkdir /opt/raspberry
cd /opt/raspberry
sudo wget https://github.com/raspberrypi/linux/zipball/f9506a194ad6a4afef06cb423286367ab787dee6w
sudo unzip f9506a194ad6a4afef06cb423286367ab787dee6w
sudo mv raspberrypi-linux-f9506a1 linux
sudo rm f9506a194ad6a4afef06cb423286367ab787dee6
cd linux

sudo wget https://raw.github.com/as00270/xbian-1.0-fs-permissions-todo/1dd59a8f8a056a833bca891c3bf94e60480cf6c8/root/patches/kernel/.config

sudo ln -s drivers/staging/media/lirc drivers/staging/lirc

sudo wget https://raw.github.com/as00270/xbian-1.0-fs-permissions-todo/1dd59a8f8a056a833bca891c3bf94e60480cf6c8/root/patches/kernel/kernel.lirc_rpi-0.2.patch
sudo patch -p1 < kernel.lirc_rpi-0.2.patch

sudo kill -9 $(pgrep xbmc)

sudo make CROSS_COMPILE=/usr/bin/ CONFIG_LIRC_STAGING=y CONFIG_LIRC_RPI=m CONFIG_I2C_DEV=m
sudo make modules CROSS_COMPILE=/usr/bin/ CONFIG_LIRC_STAGING=y CONFIG_LIRC_RPI=m CONFIG_I2C_DEV=m
sudo make modules_install CROSS_COMPILE=/usr/bin/ CONFIG_LIRC_STAGING=y CONFIG_LIRC_RPI=m CONFIG_I2C_DEV=m INSTALL_MOD_PATH=/

cp arch/arm/boot/Image /boot/kernel.img

reboot
