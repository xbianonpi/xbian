#!/bin/bash
sudo apt-get purge -y libice6 libxt6 xserver-common xserver-xorg xserver-xorg-core xserver-xorg-input-all xserver-xorg-video-fbdev xserver-xorg-input-synaptics xserver-xorg-input-evdev x11-utils x11-xkb-utils aspell lxappearance lxde lxde-common lxde-core lxde-icon-theme lxinput lxmenu-data lxpanel lxpolkit lxrandr lxsession lxsession-edit lxshortcut lxtask lxterminal gnome-icon-theme gnome-themes-standard libgnome-keyring-common libgnome-keyring0:armhf libsoup-gnome2.4-1:armhf idle desktop-base desktop-file-utils dbus-x11 dictionaries-common fbset fonts-freefont-ttf gconf2 gdb gtk2-engines:armhf hicolor-icon-theme libgdk-pixbuf2.0-0:armhf libgl1-mesa-glx:armhf menu omxplayer penguinspuzzle x11-common xdg-utils xkb-data libatasmart4:armhf libcairo-gobject2:armhf libcups2:armhf firmware-atheros firmware-ralink firmware-realtek firmware-libertas firmware-brcm80211 aptitude-common curl debconf-utils debian-reference-common debian-reference-en dphys-swapfile dpkg-dev fake-hwclock g++ gcc hardlink keyboard-configuration libaio1:armhf libatasmart4:armhf libblas3 libblas3gf libbluetooth3:armhf libboost-iostreams1.50.0 libcec1:armhf libconfuse-common libconfuse-dev libconfuse0:armhf libdrm-nouveau1a:armhf libdrm-radeon1:armhf libdrm2:armhf libgfortran3:armhf libglib2.0-data libgudev-1.0-0:armhf libiw30:armhf liblapack3  liblapack3gf libluajit-5.1-common libnl-3-200:armhf libnl-genl-3-200:armhf libpci3:armhf libpcsclite1:armhf libpolkit-gobject-1-0:armhf libsgutils2-2 libusb-1.0-0:armhf luajit menu-xdg module-init-tools ncdu pciutils pkg-config python-rpi.gpio python3 python3-minimal python3-numpy python3-rpi.gpio python3.2 python3.2-minimal raspi-copies-and-fills rsyslog shared-mime-info strace udisks usbutils wireless-tools wpasupplicant dillo fontconfig-config libaio1 libbluetooth3  libfltk1.3:armhf libfontconfig1:armhf libfreetype6:armhf libjbig2dec0 libopenjpeg2 libxext6 libxft2 libxinerama1 libxrender1 mupdf tcl8.4 ttf-dejavu-core exim4-base exim4-config exim4-daemon-light heirloom-mailx libmail-sendmail-perl libmysqlclient-dev

sudo wget http://cacing.vlsm.org/pool/main/g/geoip-database/geoip-database_20120907-1_all.deb
sudo dpkg -i geoip-database_20120907-1_all.deb
sudo rm geoip-database_20120907-1_all.deb

sudo wget http://ftp.br.debian.org/debian/pool/main/m/mysql-5.5/mysql-common_5.5.24+dfsg-9_all.deb
sudo dpkg -i mysql-common_5.5.24+dfsg-9_all.deb
sudo rm mysql-common_5.5.24+dfsg-9_all.deb

sudo wget http://cacing.vlsm.org/pool/main/m/mysql-5.5/libmysqlclient18_5.5.24%2bdfsg-9_armhf.deb
sudo dpkg -i libmysqlclient18_5.5.24+dfsg-9_armhf.deb
sudo rm libmysqlclient18_5.5.24+dfsg-9_armhf.deb

sudo apt-get install -q -y git libafpclient-dev:armhf libafpclient0:armhf libfuse2:armhf samba smbclient automake autoconf at bc bind9-host fuse geoip-database gettext gettext-base git-core html2text inetutils-syslogd libao-common libao-dev libao4 libarchive12:armhf libasprintf0c2:armhf libcdio13 libcppunit-1.12-1 libelf1 libgettextpo0:armhf libjpeg8:armhf liblircclient0 liblockdev1 libltdl7:armhf liblzo2-2 libmicrohttpd10 libmysqlclient18 libnettle4 libpcrecpp0 libplist-dev libplist1 libpython2.7 libsmbclient:armhf libssh-4:armhf libssl-dev libssl-doc libsys-hostname-long-perl libtiff4:armhf libtinyxml2.6.2 libunistring0:armhf libxml2-dev:armhf libxmlrpc-core-c3 libxmuu1:armhf libyajl2 localepurge ntfs-3g po-debconf python-dev python2.7-dev sqlite3 time fakeroot udev liblockdev1-dev libsmbclient-dev libssh-dev libavahi-client-dev libmicrohttpd-dev libtinyxml-dev libyajl-dev liblzo2-dev libjpeg-dev libpython2.7 libfribidi-dev libpcre3-dev libcdio-dev libfreetype6 


sudo apt-get autoremove -y
sudo apt-get purge -y $(dpkg --get-selections | grep deinstall | awk '{print $1}')

sudo apt-get purge -y exim4-base exim4-config exim4-daemon-light heirloom-mailx libmail-sendmail-perl

sudo rm -rf /var/cache/apt/archives/*
