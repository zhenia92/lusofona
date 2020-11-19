ip = list()
port = list()

for x in range(1,1025):
    port.append(x)

    f = open('portList.txt','a')
    f.write(str(x)+'\n')
    f.close()
    
    

for y in range(0,256):
    ip_pre = '192.168.1.' + str(y)
    ip.append(ip_pre)
    
    f = open('ipList.txt','a')
    f.write(ip_pre +'\n')
    f.close()
