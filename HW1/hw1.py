"""
Ben Bornholm
Date: 8-26-14
"""
import csv
import sys
import struct, socket

def ip2long(ip):
    try:
        packedIP = socket.inet_aton(ip)
        return struct.unpack("!L", packedIP)[0]
    except socket.error:
        pass

def main():

    if len(sys.argv) == 1:
        print "Please use: python hw1.py [filename]"
        sys.exit()

    #create a file object
    f = open(sys.argv[1],'r')
    reader = csv.reader(f)

    #dictonary for ip
    dictIP = {}

    #add each ip to dictonary
    for row in reader:
        ipNum = ip2long(str(row[3]))

        #add to dictonary ip(key) : int(value)
        dictIP[ipNum] = str(row[3])

    #sort the dictonary based on int(key)
    sorted(dictIP)
    print dictIP

    for ip in dictIP:
        print dictIP[ip]



main()
