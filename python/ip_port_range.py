#coding=utf-8

ip = list()
port = list()

for x in range(1,1025):
    port.append(x)

    f = open('portList.txt','a')
    f.write(str(x)+'\n')
    f.close()

# Debug Ports
# print(port)

# Another Way to do

#f = open('portList2.txt','a')
#portList = [(str(x)+'\n') for x in range(1,1025)]
#f.writelines(portList)
#f.close()



for y in range(0,256):
    ip_pre = '192.168.1.' + str(y)
    ip.append(ip_pre)
    
    f = open('ipList.txt','a')
    f.write(ip_pre +'\n')
    f.close()

# Debug Ports
# print(ip)

# Another Way to do

#pre_ip = '192.168.1.'
#f = open('ipList2.txt','a')
#IpList = [(pre_ip+str(x)+'\n') for x in range(0,256)]
#f.writelines(IpList)
#f.close()


