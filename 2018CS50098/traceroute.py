import os
import re

domain=input("traceroute ")
stream=os.popen(f'ping -t 1 {domain}')
output=stream.read()
array=re.findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",output)
destination=array[0]
print("traceroute to "+domain+" ("+destination+"), 64 hops max")
for ttl in range(1,33):
    stream=os.popen(f'ping -t 1 -m {ttl} {destination}')
    output=stream.read()
    array1=re.findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",output)
    ip_address=array1[2]
    stream=os.popen(f'ping -t 3 {ip_address}')
    output=stream.read()
    array2=re.findall("[0-9]*\.[0-9]*\sms",output)
    if len(array2)==0:
        time0="*"
        time1="*"
        time2="*"
    elif len(array2)==1:
        time0=array2[0]
        time1="*"
        time2="*"
    elif len(array2)==2:
        time0=array2[0]
        time1=array2[1]
        time2="*"
    else:
        time0=array2[0]
        time1=array2[1]
        time2=array2[2]
    if len(array1)==3:
        ip_address="*"
        if ttl<10:
            print(" "+str(ttl)+"  * * *")
        else:
            print(str(ttl)+"  * * *")
    else:
        if ttl<10:
            print(" "+str(ttl)+"  "+ip_address+"  "+time0+"  "+time1+"  "+time2)
        else:
            print(str(ttl)+"  "+ip_address+"  "+time0+"  "+time1+"  "+time2)
    if ip_address==destination:
        break
