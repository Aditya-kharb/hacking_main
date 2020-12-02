import scapy.all as scapy
import optparse
from scapy.all import srp
import subprocess as subp

parser = optparse.OptionParser()
parser.add_option("--ip","--ip_address",dest="ip_address",help="Enter the ip of router you want to scan")
(values,keys) = parser.parse_args()
ip_address = values.ip_address
def main(ip_address_to_scan):
    scapy.arping(ip_address_to_scan)
    
    # arp_request =  scapy.ARP(pdst=ip_address_to_scan)
    # broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # arp_request_broadcast = arp_request/broadcast
    # answered_list = srp(arp_request_broadcast,timeout=1,verbose=False)
    # print(answered_list[0])

if __name__ == "__main__":
    main(ip_address)
