#!/bin/bash
#
#Copyright 2012 CurlyMo <development@xbian.org>
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
if ! [[ -z $SSH_CONNECTION && $(who am i | grep -wo "[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*" | wc -l) -eq 0 &&  "$TERM" != "screen"  && ! -n "$TMUX" ]]; then
        if [ $(id -u) -eq 1001 ]; then
                sudo xbian-config
        fi
fi
