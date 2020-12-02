# !usr/bin/env python3
import scapy.all as scapy
def scan(ip):
    arp_requet = scapy.ARP(pdst=ip)#
    broadcast = scapy.Ether()
    scapy.ls(scapy.Ether())
    print(arp_requet.summary())
scan("192.168.0.1/24")
