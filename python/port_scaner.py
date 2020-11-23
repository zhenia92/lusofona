#coding=utf-8
import argparse
from pping import ping
import sys
import threading
import ipaddress
import socket

# Program support input for masks:
#   > 255.255.255.0
#   > 255.255.0.0
#   > 255.0.0.0

# Arugments help and check
parser = argparse.ArgumentParser()
parser.add_argument('--ip', required=True, type=str, help="Network IP Address")
parser.add_argument('--mask', required=True, type=str,help="Network Mask Address")
args = parser.parse_args()

# Ping hosts
def host_ping(host):
    try:
        p_host = ping(host,repeat=1,timeout=0.3)
        if p_host[0].status == 'ok':
            host_to_scan.append(host) 
    except KeyboardInterrupt:
        sys.exit()

# Test socket connection
def host_socket(host,port):
    try:
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a_socket.settimeout(2.0) 
        location = (host, port)
        result_of_check = a_socket.connect_ex(location)
        
        if result_of_check == 0:
            port_open.append(port)
        a_socket.close()
    except KeyboardInterrupt:
        sys.exit()

# Print Header for Ping
def print_header_ping(mask):
    if mask == '16' or mask == '8':
        if mask == 16:
            print('[+] Ping network --- '+ip_pre[0]+'.0.0.0/'+mask)
        else:
            print('[+] Ping network --- '+ip_pre[0]+'.'+ip_pre[1]+'.0.0/'+mask)
        print('[*][!] Attention it will take very long time!!!')
        print('[*][!] Recommend use scan for with 255.255.255.0 mask')
    else:
        print('[+] Ping network --- '+ip_pre[0]+'.'+ip_pre[1]+'.'+ip_pre[2]+'.0/'+mask)

# Organize threads for ping
def thread_ping(ips_list):
    try:
        threads = [threading.Thread(target=host_ping, args=(host,)) for host in ips_list]
        [t.start() for t in threads]
        [t.join() for t in threads]
    except KeyboardInterrupt:
        sys.exit()

# Organize threads for socket
def thread_socket(host,port_list):
    try:
        threads = [threading.Thread(target=host_socket, args=(host,port)) for port in port_list]
        [t.start() for t in threads]
        [t.join() for t in threads]
    except KeyboardInterrupt:
        sys.exit()
        
# Main logic
if args.ip and args.mask:
    ip = args.ip
    mask = args.mask
    host_to_scan = []
    ips_list = []

    port_list = [p for p in range(0,1025)]
    ip_pre = ip.split('.')
    mask_pre = mask.split('.')
    avabile_host = []
    if mask_pre[3] == '0' and mask_pre[2] == '0' and mask_pre[1] == '0':
        print_header_ping('8')
        for p1 in range(0,256):
            for p2 in range(0,256):
                for p3 in range(0,256):
                    ips_list = [ip_pre[0]+'.'+str(p1)+'.'+str(p2)+'.'+str(p3)]

        thread_ping(ips_list)
        l = sorted(host_to_scan, key = ipaddress.IPv4Address)
        print('[+] Hosts online in network')
        [print('[-] '+ip) for ip in l]

    elif mask_pre[3] == '0' and mask_pre[2] == '0':
        print_header_ping('16')
        for p1 in range(0,256):
            for p2 in range(0,256):
                ips_list.append(ip_pre[0]+'.'+ip_pre[1]+'.'+str(p1)+'.'+str(p2))
        thread_ping(ips_list)
        l = sorted(host_to_scan, key = ipaddress.IPv4Address)
        print('[+] Hosts online in network')
        [print('[-] '+ip) for ip in l]
       
    elif mask_pre[3] == '0':
        print_header_ping('24')
        ips_list = [ip_pre[0]+'.'+ip_pre[1]+'.'+ip_pre[2]+'.'+str(i) for i in range(1,255)]
        thread_ping(ips_list)
        l = sorted(host_to_scan, key = ipaddress.IPv4Address)
        print('[+] Hosts online in network')
        [print('[-] '+ip) for ip in l]

    f = open('ports_open.txt','a')
    for host in l:
        port_open = []
        print('[+] Scanning ports opened on host '+host)
        thread_socket(host,port_list)        
        [print('[-][-] Port '+str(port)+' is open.') for port in port_open]
        [f.write(str(host)+':'+str(port)+'\n') for port in port_open]
    f.close()