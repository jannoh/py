#!/usr/bin/env python
import subprocess

interface = 'wlan0'
new_mac_addr = '00:11:22:33:44:77'

print(f"[+] Changing MAC Address for {interface} to {new_mac_addr}")

subprocess.call(f'ifconfig {interface}', shell=True)
subprocess.call(f'ifconfig {interface} hw ether {new_mac_addr}', shell=True)
subprocess.call(f'ifconfig {interface} up', shell=True)