import random
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