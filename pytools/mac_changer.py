#!/usr/bin/env python
import subprocess

interface = input('interface::> ')
new_mac_addr = input('new MAC::> ')

print(f"[+] Changing MAC Address for {interface} to {new_mac_addr}")

subprocess.call(['ifconfig',interface,'down'])
subprocess.call(['ifconfig',interface,'hw','ether', new_mac_addr])
subprocess.call(['ifconfig',interface,'up'])