import scapy.all as scapy
from scapy.layers.dns import DNS
import netfilterqueue 

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload()) 
    if scapy_packet.haslayer(DNS):
        qname = scapy_packet[scapy.DNSQR].qname
        qname_d = qname.decode("utf")
       # if qname == 'www.bing.com':
        print(qname_d)
    # # if scapy_packet.haslayer(scapy.IP):
    # #     ip_name = scapy_packet[scapy.IP].dst 
        #print(scapy_packet.show())
    packet.accept()
queue = netfilterqueue.NetfilterQueue()
queue.bind(0 , process_packet)
queue.run()