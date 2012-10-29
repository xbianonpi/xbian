#!/bin/bash

#Removing unnecessary packages and installing required packages
sudo apt-get update

sudo apt-get purge -y libice6 libxt6 xserver-common xserver-xorg xserver-xorg-core xserver-xorg-input-all xserver-xorg-video-fbdev xserver-xorg-input-synaptics xserver-xorg-input-evdev x11-utils x11-xkb-utils aspell lxappearance lxde lxde-common lxde-core lxde-icon-theme lxinput lxmenu-data lxpanel lxpolkit lxrandr lxsession lxsession-edit lxshortcut lxtask lxterminal gnome-icon-theme gnome-themes-standard libgnome-keyring-common libgnome-keyring0:armhf libsoup-gnome2.4-1:armhf idle desktop-base desktop-file-utils dbus-x11 dictionaries-common fbset fonts-freefont-ttf gconf2 gdb gtk2-engines:armhf hicolor-icon-theme libgdk-pixbuf2.0-0:armhf libgl1-mesa-glx:armhf menu omxplayer penguinspuzzle x11-common xdg-utils xkb-data libatasmart4:armhf libcairo-gobject2:armhf libcups2:armhf firmware-atheros firmware-ralink firmware-realtek firmware-libertas firmware-brcm80211 aptitude-common curl debconf-utils debian-reference-common debian-reference-en dphys-swapfile dpkg-dev fake-hwclock g++ gcc hardlink \
keyboard-configuration libatasmart4:armhf libblas3 libblas3gf libbluetooth3:armhf libboost-iostreams1.50.0 libdrm2:armhf libgfortran3:armhf libglib2.0-data libgudev-1.0-0:armhf libiw30:armhf liblapack3 liblapack3gf libluajit-5.1-common libnl-3-200:armhf libnl-genl-3-200:armhf libpci3:armhf libpcsclite1:armhf libpolkit-gobject-1-0:armhf libsgutils2-2 libusb-1.0-0:armhf luajit menu-xdg module-init-tools ncdu pciutils pkg-config python-rpi.gpio python3 python3-minimal python3-numpy python3-rpi.gpio python3.2 python3.2-minimal raspi-copies-and-fills rsyslog shared-mime-info strace udisks usbutils wireless-tools wpasupplicant dillo fontconfig-config libbluetooth3 libfltk1.3:armhf libfontconfig1:armhf libfreetype6:armhf libjbig2dec0 libopenjpeg2 libxext6 libxft2 libxinerama1 libxrender1 mupdf ttf-dejavu-core fuse gettext-base libasprintf0c2 libasyncns0 libaudit0 libcaca0 libdirectfb-1.2-9 libflac8 libfm-data libfuse2 libgif4 libid3tag0 libjavascriptcoregtk-3.0-0 libjson0 libmad0 libmenu-cache1 libmikmod2 \
libmtdev1 libogg0 libpciaccess0 libportmidi0 libsndfile1 libts-0.0-0 libvorbis0a libvorbisenc2 libvorbisfile3 libvte-common libwebkitgtk-3.0-common libwebp2 libwnck-common libxkbfile1 python-support tcl8.5 tsconf zenity-common libswitch-perl* perl* perl-modules* tasksel* tasksel-data* libept1.4.12* libxapian22* libxau6* libxcb1* libxdmcp6:armhf raspi-config triggerhappy ed kbd krb5-locales alsa-base alsa-utils gcc-4.4-base:armhf gcc-4.5-base:armhf gcc-4.6 gcc-4.6-base libasound2 libgomp1 libsamplerate0 triggerhappy libtagcoll2-dev libgmp10 libmpc2 libmpfr4 libtirpc1 libp11-kit0 libswitch-perl* perl* perl-modules* tasksel* tasksel-data* libx11-data libxau6 libxcb1 libxdmcp6 make libx11-6* tk8.4* libsmbclient:armhf libssh-4:armhf

sudo apt-get install screen git dialog libsamplerate0 libmysqlclient18 libsmbclient libssh-4 lib libavahi-client-dev libmicrohttpd-dev libtinyxml-dev libyajl-dev liblzo2-dev libjpeg-dev libpython2.7 libfribidi-dev libpcre3-dev libcdio-dev libfreetype6

sudo apt-get autoremove -y

sudo apt-get purge -y $(dpkg --get-selections | grep deinstall | awk '{print $1}')

sudo apt-get purge -y exim4-base exim4-config exim4-daemon-light heirloom-mailx libmail-sendmail-perl

sudo rm -rf /var/cache/apt/archives/*


#Setting up xbian user and deleting pi user
sudo su
useradd -G sudo -m -s /bin/bash xbian
echo "xbian:raspberry" | chpasswd

# Relogin with ssh; user:xbian pass:raspberry

#Kill all processes started by user pi
for i in $(pgrep -u pi); do kill -9 $i; done;

#Deleting user pi
sudo su
userdel pi
rm -rf /home/pi

#Disabling root login
sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config

#Set hostname
echo "xbian" > /etc/hostname
hostname xbian
sed -i 's/raspberrypi/xbian/g' /etc/hosts

#Clone xbian git
cd /home/xbian/
git clone --depth 1 https://github.com/Koenkk/xbian.git source
cd source

#Installation
cp -R etc/* /etc/
cp -R usr/* /usr/
rm -rf /lib/modules/*
cp -R lib/* /lib/
rm -rf /boot/*
cp -R boot/* /boot/
#cp -r home/* /home/
rm -rf /opt/vc
cp -r opt/vc /opt

# Correcting permissions
chmod +x /etc/init.d/*
chmod +x /usr/local/sbin/*
chmod +x /usr/local/bin/*
chmod +x /usr/local/lib/xbmc/xbmc.bin
chown -hR xbian /home/xbian

#Update rc.d
update-rc.d xbmc defaults
update-rc.d xbian defaults
update-rc.d lirc defaults
update-rc.d rpcbind defaults

#Fixing broken symbolic links
rm /usr/local/lib/libtag_c.so.0
ln -s /usr/local/lib/libtag_c.so.0.0.0 /usr/local/lib/libtag_c.so.0
rm /usr/local/lib/libshairport.so.0
ln -s /usr/local/lib/libshairport.so.0.0.0 /usr/local/lib/libshairport.so.0
rm /usr/local/lib/libtag.so.1
ln -s /usr/local/lib/libtag.so.1.12.0 /usr/local/lib/libtag.so.1

# Set locale to c to prevent weird characters in xbian-config and c compiling
export LANG=C
export LC_ALL=C
export LANGUAGE=C

#Remove user pi from sudoers and add xbian user
sed -i '$d' /etc/suoders > /etc/suoders
echo "xbian ALL=(ALL) NOPASSWD: /usr/local/sbin/xbian-config, /sbin/halt, /sbin/reboot" >> /etc/sudoers

#Delete auto start of raspi-config
rm /etc/profile.d/raspi-config.sh