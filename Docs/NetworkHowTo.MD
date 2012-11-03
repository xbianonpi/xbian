Ethernet
=============================
- DHCP, full content of /etc/network/interfaces
auto lo
iface lo inet loopback

iface eth0 inet dhcp

- Static ip, full content of /etc/network/interfaces
auto lo
iface lo inet loopback

iface eth0 inet static
address 192.168.0.10
network 192.168.0.0
netmask 255.255.255.0
broadcast 192.168.0.255
gateway 192.168.0.1



Wireless
============================
- DHCP, full content of /etc/network/interfaces
auto lo

iface lo inet loopback
iface eth0 inet dhcp

allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
wireless-power off
iface default inet dhcp

- Static ip, full content of /etc/network/interfaces
auto lo

iface lo inet loopback
iface eth0 inet dhcp

allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
address 192.168.0.10
network 192.168.0.0
netmask 255.255.255.0
broadcast 192.168.0.255
gateway 192.168.0.1
wireless-power off
iface default inet dhcp



- WPA/WPA2 & WEP Security, full content of /etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
ssid="ssidofmynetwork"
psk="passofmynetwork"
}

- Unprotected, full content of /etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
ssid="ssidofmynetwork"
}
