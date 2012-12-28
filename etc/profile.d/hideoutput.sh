#!/bin/bash
#
#Copyright 2012 CurlyMo <development@xbian.org>
#
#This file is part of Xbian - XBMC on the Raspberry Pi.
#
#Xbian is free software: you can redistribute it and/or modify it under the 
#terms of the GNU General Public License as published by the Free Software 
#Foundation, either version 3 of the License, or (at your option) any later 
#version.
#
#Xbian is distributed in the hope that it will be useful, but WITHOUT ANY 
#WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
#FOR A PARTICULAR PURPOSE. See the GNU General Public License for more 
#details.
#
#You should have received a copy of the GNU General Public License along 
#with Xbian. If not, see <http://www.gnu.org/licenses/>
#
if [[ $(who am i | awk '{print $2}') == "tty1" ]]; then

	# Hide console output
        clear
        export PS1="\e[40;30m";
        echo -e '\e[40;30m';

else

        # Restore console output
        export PS1="\[\e[40;0m\]\u@\h:\w# "
        echo -e '\e[40;0m';

        # Reset/Restore framebuffer
        GEO=$(sudo fbset -s | grep geometry);GEO_ARR=($GEO);
        if [ ${#GEO_ARR[@]} -eq 6 ]; then
                XRES=$(echo $GEO | cut -f 2 -d" ")
                YRES=$(echo $GEO | cut -f 3 -d" ")
                VXRES=$(echo $GEO | cut -f 4 -d" ")
                VYRES=$(echo $GEO | cut -f 5 -d" ")
                DEPTH=$(echo $GEO | cut -f 6 -d" ")
                sudo fbset -xres $XRES -yres $YRES -vxres $VXRES -vyres $VYRES -depth $DEPTH
        fi

fi
