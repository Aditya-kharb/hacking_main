#yean this work on local machine like a malware
import scapy.all as scapy
import netfilterqueue 
from scapy.layers import http

# subp.call("sudo iptables -I INPUT -j NFQUEUE --queue-num 0",shell=True)
# subp.call("sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0",shell=True)
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload()) 
    if scapy_packet.haslayer(http.Raw):
        if scapy_packet[scapy.TCP].sport == 80:
            print(scapy_packet.show())
        if scapy_packet[scapy.TCP].dport == 80:
            print("this is http request")
    packet.accept()
queue = netfilterqueue.NetfilterQueue()
queue.bind(0 , process_packet)
queue.run() 