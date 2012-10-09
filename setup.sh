#!/bin/bash

apt-get install unzip

wget https://github.com/as00270/xbian-1.0-fs-permissions-todo/zipball/master
mv master xbian.zip
unzip xbian.zip
cd as00270-xbian-1.0-fs-permissions-todo-*
mv -R etc/* /etc/
mv -R usr/* /usr/

#Setup init scripts
update-rc.d resizesd start 2
update-rc.d xbmc defaults
update-rc.d xbian defaults
