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
if [[ -z $SSH_CONNECTION && $(who am i | awk '{print $2}') == "tty1" && $(who am i | grep -wo "[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*" | wc -l) -eq 0 && "$(who am i | awk '{print $1}')" == "$(id -urn)" && "$TERM" != "screen" && ! -n "$TMUX" ]]; then
        clear
	export PS1="\e[40;30m";
	echo -e '\e[40;30m';
fi
