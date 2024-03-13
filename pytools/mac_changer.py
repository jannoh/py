#!/usr/bin/env python
import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option('-i', "--interface", dest='interface', help='Interface to change host MAC address')
parser.add_option('-m', "--mac", dest='new_mac', help='New MAC Address')

(cli_values, cli_flags) = parser.parse_args()

interface = cli_values.interface
new_mac_addr = cli_values.new_mac

print(f"[+] Changing MAC Address for {interface} to {new_mac_addr}")

subprocess.call(['ifconfig',interface,'down'])
subprocess.call(['ifconfig',interface,'hw','ether', new_mac_addr])
subprocess.call(['ifconfig',interface,'up'])