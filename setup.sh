#!/bin/bash

#11-10-2012 21:39
#Setting up xbian user and deleting pi user
sudo useradd -G sudo -m -s /bin/bash xbian
sudo echo "xbian:raspberry" | chpasswd

#Deleting user pi
sudo userdel pi
sudo rm -rf /home/pi

#11-10-2012 23:15
#Disabling root login
sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config

#Set hostname
echo "xbian" > /etc/hostname
hostname xbian

#09-10-2012 22:00
#Installing and dowloading git files
apt-get install unzip

wget https://github.com/as00270/xbian-1.0-fs-permissions-todo/zipball/master
mv master xbian.zip
unzip xbian.zip
cd as00270-xbian-1.0-fs-permissions-todo-*
mv -R etc/* /etc/
mv -R usr/* /usr/

#09-10-2012 22:00
#Setup init scripts
update-rc.d resizesd start 2
update-rc.d xbmc defaults
update-rc.d xbian defaults
