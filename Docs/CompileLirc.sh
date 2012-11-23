#!/bin/bash
#
#Copyright 2012 CurlyMo <development@xbian.org>, 
#Aron Robert Szabo <aron@reon.hu>
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
cd /usr/src
sudo git clone --depth 5 https://github.com/raspberrypi/tools.git
cd tools
sudo git checkout 9c3d7b6ac692498dd36fec2872e0b55f910baac1
sudo ln -s /usr/src/tools/arm-bcm2708/arm-bcm2708-linux-gnueabi/bin/arm-bcm2708-linux-gnueabi-gcc /usr/bin/arm-bcm2708-linux-gnueabi-gcc

#Install lirc for the default configuration files
sudo apt-get install autoconf automake libtool gcc help2man lirc
#Remove lirc because it will be replaced by a custom compiled version
sudo apt-get remove lirc

cd /usr/src
sudo git clone --depth 5 git://lirc.git.sourceforge.net/gitroot/lirc/lirc
cd lirc
sudo ./autogen.sh
sudo wget https://raw.github.com/Koenkk/xbian/master/Patches/lirc/02-lirc_xbian.patch
sudo wget https://raw.github.com/Koenkk/xbian/master/Patches/lirc/03-lirc_xbian.patch
sudo wget https://raw.github.com/Koenkk/xbian/master/Patches/lirc/04-lirc_xbian.patch
sudo wget https://raw.github.com/Koenkk/xbian/master/Patches/lirc/05-lirc_xbian.patch
sudo patch -p1 < 02-lirc_xbian.patch
sudo patch -p1 < 03-lirc_xbian.patch
sudo patch -p1 < 04-lirc_xbian.patch
sudo ./configure --with-driver=all CROSS_COMPILE=/usr/bin/
sudo make CROSS_COMPILE=/usr/bin/ LC_CTYPE=en_US.UTF-8
sudo make install CROSS_COMPILE=/usr/bin/ LC_CTYPE=en_US.UTF-8

