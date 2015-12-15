"""
Author: Ben Bornholm
Date: 9-9-15
Description:
"""
from bs4 import BeautifulSoup
import re
import sys
import urllib2

def main():
    if len(sys.argv) == 0:
        print "Please use python weblinker.py <html>"
        sys.exit()

    #Create file
    f = open('weblink.html','w')

    #Grab html code
    print sys.argv[1]
    html_page = urllib2.urlopen(sys.argv[1])
    soup = BeautifulSoup(html_page,"html.parser")
    for link in soup.findAll('a'):
        #Make sure string is not emepty
        if link.get('href') != None and link.get('href') != "#" and 'http://' in link.get('href'):
            f.write(link.get('href'))
            #Print web link
            webpage = link.get('href')

            try:
                a = urllib2.urlopen(webpage)
                print webpage
            except urllib2.HTTPError as e :
                print "404 error"


    #Close text file
    f.close()



main()
