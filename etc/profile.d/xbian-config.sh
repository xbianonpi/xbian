#!/bin/bash
if [ `/usr/bin/id -u` != "0" ]; then
        sudo xbian-config
fi
