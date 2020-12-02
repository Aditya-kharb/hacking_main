#!usr/bin/env python3.7
#number of outputs = 1
#--------------------------------------------
import subprocess as subp
import optparse
import random
#this show us ifconfig results
i = 0
list_1 = []
list_2 = []
while(i<14):
    rand_int = random.choice("abcdefghij0123456789")
    list_1.append(rand_int)
    i += 1 
# print(list_1)
mac_address = ""
with open("test.txt","w") as wri:
    wri.write("")
for x in range(0,10):
    x += 2
    list_2.append(list_1[x]+list_1[x+1]+":")
for i in range(0,6):
    list_2[5] = "0e"
    #print(list_2[i])
    with open("test.txt","a") as f:
        f.write(list_2[i])
with open("test.txt","r") as red:
    res = red.read(100)
    print(res)
# parser = optparse.OptionParser()
# parser.add_option("--i","--interface",dest="interface",help="This will change mac address")
# (options,args) = parser.parse_args()
def Mac_changer():
    subp.call("ifconfig",shell=True)
    subp.check_output("ifconfig")
    # ask_down_eth_port = input("[*ENter THe DEvice TO TAke DOwn*] >")
    # out_put_1 = subp.check_output(["ifconfig",ask_down_eth_port])
    # print(out_put_1)
    subp.call("sudo ifconfig wlan0 down",shell=True)
    subp.call("sudo ifconfig wlan0 hw ether "+res,shell=True)
    subp.call("sudo ifconfig wlan0 up",shell=True)
    see_out = subp.check_output(['ifconfig','wlan0'])
    print(see_out)
Mac_changer()