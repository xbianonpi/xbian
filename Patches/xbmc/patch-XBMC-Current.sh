#
#Copyright 2012 Koen Kanters, Raspbian
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
PATCHES="TPNno.patch
EGLRes.patch
XBianSysSum.patch
NetworkCachingRedux.patch
RemoveGUISoundSettings.patch
WOL.patch
Splash.patch"
for patch in $PATCHES
do
  wget https://raw.github.com/xbianonpi/xbian/xbian-alpha5/Patches/xbmc/$patch -O $patch
  patch -p1 < $patch
  rm $patch
done
