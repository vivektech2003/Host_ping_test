import subprocess
import os

def Ping_Host_IP(ip):

    with open(os.devnull, "wb") as limbo:
        result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],stdout=limbo, stderr=limbo).wait()
        if result:
            #print ip, "inactive"
            return ip + " ->Failed"
        else:
            #print ip, "active"
            return ip + " ->Ok"

#output=Ping_Host_IP('127.0.0.1')
#print output

with open('host_list') as host:
    for ip in host:
        print Ping_Host_IP(ip.strip())
