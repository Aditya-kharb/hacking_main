# i donot know why this shit is not working
import optparse
import scapy.all as scapy
from scapy.layers import http


def sniff_packets(interface):
    #sniff the data extrcted from website
    scapy.sniff(iface=interface,store=False,prn=process_sniff_packet,filter="udp")
def process_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = scapy.get_url(packet)
        print(url)

sniff_packets("wlan0")
