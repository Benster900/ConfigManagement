"""
Author: Ben Bornholm
Date: 9-23-15
Description:
"""

import os
from collections import defaultdict

def main():
    output = os.popen('netstat --inet --numeric -anop')

    #Create dictonary for local ports
    dictPort = {}

    #Create list  for PIDs
    dictPID = []

    #List of PIDs
    listPID= []

    #List of values for PIDs
    listPIDvales =[]

    for line in output.readlines():
        temp = line.split()

        #For UDP
        if len(temp) == 8:
            proto=temp[0] #grabs protcol

            #Local port
            localAddr = temp[3]
            if '[' in localAddr:
                localPort = localAddr[localAddr.find(']')+2:] #grabs port for ipv6
            else:
                localPort = localAddr[localAddr.find(':')+1:]  #grabs port for ipv4

            #PID
            pid = "0"

            dictPort[int(localPort.strip())] = "%s\t%s\t%s\t%s\t\t%s"%(localPort,"*.*",proto,"empty",pid)
            str2 = "%s\t%s\t%s\t%s\t\t%s"%(localPort,"*.*",proto,"empty",pid)
            tuple1=(pid,str2)
            dictPID.append(tuple1)

        #For TCP
        if 	len(temp) == 9:
            proto = temp[0] #grabs protcol

            #local port
            localAddr = temp[3]
            if ']' in localAddr:
                localPort = localAddr[localAddr.find(']')+2:].strip() #grabs port
            else:
                localPort = localAddr[localAddr.find(':')+1:].strip() #grabs port

            #remote ports
            foreignAddr = temp[4]
            if ']' in foreignAddr:
                remotePort = foreignAddr[foreignAddr.find(']')+2:].strip() #grabs port
            else:
                remotePort = foreignAddr[foreignAddr.find(':')+1:].strip() #grabs port

            #state and pid
            state = temp[5] #grabs state

            #PID
            str1 = temp[6]
            if '/' in str1:
                pid = str1[:str1.find('/')] #grabs PID
            else:
                pid = "\t0"

            dictPort[int(localPort.strip())] = "%s\t%s\t%s\t%s\t%s"%(localPort,remotePort,proto,state,pid)
            str2 = "%s\t%s\t%s\t%s\t%s"%(localPort,remotePort,proto,state,pid)
            tuple1=(pid,str2)
            dictPID.append(tuple1)

    print "Sorted by Local Ports"
    print"Local\tRemote\tProto\tState\t\tPID"
    for key in sorted(dictPort.iterkeys()):
            print "%s"%(dictPort[key])

    print "\n\nSorted by PIDs"
    print"Local\tRemote\tProto\tState\t\tPID"
    for x in sorted(dictPID):
        print x[1]



main()
