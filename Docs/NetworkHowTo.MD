Ethernet static IP
=============================
In /etc/network/interfaces

DHCP example:
auto eth0
iface eth0 inet dhcp

Static IP example:
auto eth0
iface eth0 inet static
address 192.168.0.
network 192.168.0.0
netmask 255.255.255.0
broadcast 192.168.0.255
gateway 192.168.0.1

Wireless NOT COMPLETED YET, MAY CHANGE!!
============================

Unprotected; add this to /etc/network/interfaces:
allow-hotplug wlan0
auto wlan0
iface wlan0 inet dhcp
wireless-essid "SSIDHERE"

WEP; add this to /etc/network/interfaces:
allow-hotplug wlan0
auto wlan0
iface wlan0 inet dhcp
wireless-essid "SSIDHERE"
wireless-key "KEYHERE"

WPA and WPA2; add this to /etc/network/interfaces:
allow-hotplug wlan0
auto wlan0
iface wlan0 inet dhcp
wpa-ssid "SSIDHERE"
wpa-psk "KEYHERE"


Wireless static ip example:
allow-hotplug wlan0
auto wlan0
iface wlan0 inet dhcp
wpa-ssid/wireless-essid "SSIDHERE"
wpa-psk/wireless-key "KEYHERE"
address 192.168.0.100
network 192.168.0.0
netmask 255.255.255.0
broadcast 192.168.0.255
gateway 192.168.0.1

