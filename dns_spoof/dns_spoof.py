import scapy.all as scapy
import netfilterqueue 

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload()) 
    if scapy_packet.haslayer(scapy.DNSRR):
        #qname = scapy_packet[scapy.DNSQR].qname
        print(scapy_packet.show())
        # print(qname)

    packet.accept()
queue = netfilterqueue.NetfilterQueue()
queue.bind(0 , process_packet)
queue.run()
process_packet()