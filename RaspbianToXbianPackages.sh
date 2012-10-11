#!/bin/bash
sudo apt-get purge -y xserver-*
sudo apt-get purge -y x11-utils
sudo apt-get purge -y x11-xkb-utils
sudo apt-get autoremove -y
sudo apt-get purge aspell
sudo apt-get purge lxappearance lxde lxde-common lxde-core lxde-icon-theme lxinput lxmenu-data lxpanel lxpolkit lxrandr lxsession lxsession-edit lxshortcut lxtask lxterminal
sudo apt-get autoremove -y
sudo apt-get purge -y gnome-icon-theme gnome-themes-standard libgnome-keyring-common libgnome-keyring0:armhf libsoup-gnome2.4-1:armhf idle
sudo apt-get autoremove -y
sudo apt-get purge -y desktop-base desktop-file-utils
sudo apt-get autoremove -y
sudo apt-get purge -y dbus-x11
sudo apt-get purge -y dictionaries-common fbset fonts-freefont-ttf 
sudo apt-get autoremove -y
sudo apt-get purge -y gconf2 gdb gtk2-engines:armhf 
sudo apt-get autoremove -y
sudo apt-get purge -y hicolor-icon-theme libgdk-pixbuf2.0-0:armhf
sudo apt-get autoremove -y
sudo apt-get purge -y libgl1-mesa-glx:armhf libx11-data 
sudo apt-get autoremove -y
sudo apt-get purge -y menu omxplayer penguinspuzzle x11-common xdg-utils xkb-data
sudo apt-get autoremove -y
sudo apt-get purge -y libatasmart4:armhf libcairo-gobject2:armhf libcups2:armhf
sudo apt-get purge -y $(dpkg --get-selections | grep deinstall | awk '{print $1}')
sudo apt-get purge -y firmware-*

sudo apt-get install -y git libafpclient-dev:armhf libafpclient0:armhf libaio1:armhf libbluetooth3:armhf libcec1:armhf libconfuse-common libconfuse-dev libconfuse0:armhf libdrm-nouveau1a:armhf libdrm-radeon1:armhf libdrm2:armhf libfuse2:armhf samba smbclient usbmount automake autoconf
sudo apt-get purge -y aptitude-common curl debconf-utils debian-reference-common debian-reference-en dphys-swapfile dpkg-dev fake-hwclock g++ gcc hardlink keyboard-configuration libaio1:armhf libatasmart4:armhf libblas3 libblas3gf libbluetooth3:armhf libboost-iostreams1.50.0 libcec1:armhf libconfuse-common libconfuse-dev libconfuse0:armhf libdrm-nouveau1a:armhf libdrm-radeon1:armhf libdrm2:armhf libgfortran3:armhf libglib2.0-data libgudev-1.0-0:armhf libiw30:armhf liblapack3  liblapack3gf libluajit-5.1-common libnl-3-200:armhf libnl-genl-3-200:armhf libpci3:armhf libpcsclite1:armhf libpolkit-gobject-1-0:armhf libsgutils2-2 libusb-1.0-0:armhf luajit menu-xdg module-init-tools ncdu pciutils pkg-config python-rpi.gpio python3 python3-minimal python3-numpy python3-rpi.gpio python3.2 python3.2-minimal raspi-copies-and-fills rsyslog shared-mime-info strace udisks usbutils wireless-tools wpasupplicant
sudo apt-get install -y at bc bind9-host fuse geoip-database gettext gettext-base git-core html2text inetutils-syslogd libao-common libao-dev libao4 libarchive12:armhf libasprintf0c2:armhf libcdio13 libcppunit-1.12-1 libelf1 libgettextpo0:armhf libjpeg8:armhf liblircclient0 liblockdev1 libltdl7:armhf liblzo2-2 libmicrohttpd10 libmysqlclient18 libnettle4 libpcrecpp0 libplist-dev libplist1 libpython2.7 libshairport-dev:armhf libshairport1:armhf libsmbclient:armhf libssh-4:armhf libssl-dev libssl-doc libsys-hostname-long-perl libtiff4:armhf libtinyxml2.6.2 libunistring0:armhf libxml2-dev:armhf libxmlrpc-core-c3 libxmuu1:armhf libyajl2 localepurge ntfs-3g po-debconf python-dev python2.7-dev sqlite3 time
sudo apt-get autoremove -y

sudo wget http://ftp.us.debian.org/debian/pool/main/libc/libcroco/libcroco3_0.6.6-1_armhf.deb
dpkg -i libcroco3_0.6.6-1_armhf.deb
rm libcroco3_0.6.6-1_armhf.deb
