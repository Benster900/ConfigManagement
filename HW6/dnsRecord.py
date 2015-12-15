"""
Author: Ben Bornholm
Date: 9-23-15
Description: A script that writes a c
omplete set of DNS records; note-create 2 MX records
and two A records: there is an A record for each MX record. Write your records to a file
named DNS.txt
"""
import sys

def main():
    #Create a file for DNS records
    f = open('DNS.txt','w')

    zone = sys.argv[1]  #domain name
    ttl = '3600'       #defualt ttl

    message ="    ; %s\n\
    $TTL %s\n\
    @   IN  SOA %s. admin.%s. (\n\
                    2012040301  ; Serial\n\
                    3600        ; Refresh\n\
                    600         ; Retry\n\
                    86400       ; Expire\n\
                    3600 ) ; Minimum\n\
    %s.         7200    IN      NS  s1.%s.\n\
    www.%s\t600     IN      A   10.2.3.4\n\
    www.%s\t600     IN      A   10.4.5.6\n\
    info.%s.\t3600   IN   CNAME   www.%s.\n\
    %s.      IN      MX  10  mail1.%s\n\
    %s.      IN      MX  20  mail2.%s\n"%(zone,ttl,zone,zone,zone,zone,zone,zone,zone,zone,zone,zone,zone,zone)

    f.write(message)
    f.close()



main()
