#!/usr/bin/env python
import subprocess
import optparse

def change_mac_addr(interface, new_mac_addr):
    print(f"[+] Changing MAC Address for {interface} to {new_mac_addr}")
    subprocess.call(['ifconfig',interface,'down'])
    subprocess.call(['ifconfig',interface,'hw','ether', new_mac_addr])
    subprocess.call(['ifconfig',interface,'up'])

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', "--interface", dest='interface', help='Interface to change host MAC address')
    parser.add_option('-m', "--mac", dest='new_mac', help='New MAC Address')
    cli_values, cli_flags = parser.parse_args()
    if not cli_values.interface:
        parser.error('[-] Please specify an interface, use --help for more info.')
    if not cli_values.new_mac:
        parser.error('[-] Please specify an new mac address, use --help for more info.')
    return cli_values

cli_values = get_arguments()
change_mac_addr(cli_values.interface, cli_values.new_mac)