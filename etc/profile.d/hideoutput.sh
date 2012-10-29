#!/bin/bash
if [ $(who am i | grep -wo "[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*" | wc -l) -eq 0 ]; then
        echo -e '\e[40;30m'
        dmesg -n 1
        clear
fi
