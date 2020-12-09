import subprocess as subp
# import optparse

# parser = optparse.OptionParser()
# parser.add_option("--i",dest="interface",help="ENter INterface TO EXtract mac_ADDress")
# (value,keys) = parser.parse_args()
# interface = value.interface

# see_out = subp.check_output(['ifconfig','wlan0'])
# print(see_out[222:239].decode("utf"))
# # for x in range(0,300):
# #     see_out.decode("utf")
# #     store_temp_1 = see_out[x]
# #     store_temp_2 = see_out[x+1]
# #     if (store_temp_1 != 'f' and store_temp_2 != '4'):
# #         print('Nf\n')
# #     else:
# #         # print(see_out[x])
# #         print("yes it is ")
# def mac_extractor():
#     print("your mac_address is :"+see_out[222:239].decode("utf"))
# mac_extractor()
resol = subp.check_output(['ifconfig','wlan0'])
resol_d = resol.decode("utf")
print(type(resol_d))