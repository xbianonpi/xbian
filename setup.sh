#!/bin/bash

#11-10-2012 21:39
#Setting up xbian user and deleting pi user
sudo su
useradd -G sudo -m -s /bin/bash xbian
echo "xbian:raspberry" | chpasswd

#Relogin with ssh as xbian user

#Kill all processes started by user pi
for i in $(pgrep -u pi); do kill -9 $i; done;

#Deleting user pi
userdel pi
rm -rf /home/pi

#11-10-2012 23:15
#Disabling root login
sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config

#Set hostname
echo "xbian" > /etc/hostname
hostname xbian
sed -i 's/raspberrypi/xbian/g' /etc/hosts

#09-10-2012 22:00
#Installing and dowloading git files
apt-get install unzip

cd /home/xbian/
git clone --depth 1 https://github.com/Koenkk/xbian.git source
cd source
cp -R etc/* /etc/
cp -R usr/* /usr/

#16-10-2012 10:40
rm -rf /lib/modules/*
cp -R lib/* /lib/
rm -rf /boot/*
cp -R boot/* /boot/

#09-10-2012 22:00
#Setup init scripts
update-rc.d resizesd start 2
update-rc.d xbmc defaults
update-rc.d xbian defaults
chmod +x /etc/init.d/lirc
chmod +x /usr/local/sbin/*
chmod +x /usr/local/bin/*
chmod +x /usr/bin/*
update-rc.d lirc defaults

#22-10-2012 14:40
#Copying home folder
cp -r home/* /home/
