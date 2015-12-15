"""
Author: Ben Bornholm
Date: 9-30-15
Description: Write a script that will "ping" a range of ip addresses. For a range of addresses use the addresses of
the machines in the lab. If your script receives a sucessful return from a machine, include that address in a list of
active machine addresses.

For each active machine address on the room network, perform a port scan. Produce an output file that lists an
'open' ports for each machine
"""

import sys
from scapy.all import *

def main():

    	ip = str(raw_input("Enter network address to scan(Ex: 192.168.1.0/24): "))
	    maxPort = int(raw_input("Enter max(65535) port to scan to: "))
    	#List of live hosts
    	pcList = []

    	#file to write output to
    	f = open('scan.txt','w')
    	f.write("List of active computers\n")

    	#Scans host on the newtork supplies
	try:
		alive,dead=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, verbose=0)
	 	print "MAC -------------------- IP"
	    	f.write("MAC------------------------IP\n")
		for i in range(0,len(alive)):
            		pcList.append(alive[i][1].psrc)
            		f.write(alive[i][1].hwsrc + " - " + alive[i][1].psrc + "\n")
        		print alive[i][1].hwsrc + " - " + alive[i][1].psrc
    	except:
	       pass

	print("--------------------------------\n\n")
    	f.write("--------------------------------\n\n")

    	#For each live pc
    	for remoteIP in pcList:
        	#output
        	print ("Port Scanning "+remoteIP)
        	f.write("Port sanning: "+remoteIP+"\n")

        	#scan all ports on a live host
        	try:
            		for port in range(1,maxPort):
                		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                		result = sock.connect_ex((remoteIP, port))
                		if result == 0:
                    			f.write("Port {}: \t Open".format(port)+"\n")
					print "Port {}: \t Open".format(port)
                    			sock.close()

        	except KeyboardInterrupt:
            		print "You pressed Ctrl+C"
            		sys.exit()

        	except socket.gaierror:
            		print 'Hostname could not be resolved. Exiting'
            		sys.exit()

        	except socket.error:
            		print "Couldn't connect to server"
            		sys.exit()

		f.write("\n")
		print("\n")
        print("------------------------\n\n")
        f.write("------------------------\n\n")



main()
