"""
Author: Ben Bornholm
Date: 10-14-15
Description: Using as scripting language, like python, create a script to download a video file and start the video playing
in a compatible video player. The URL for the video file will come from the command line.

Modift the your script to accept a list of video URL's to download. The list of videos URL's will come from a text file. The
name of the file will come from the command line.

website: https://ia801006.us.archive.org/32/items/electricsheep-flock-244-80000-7/00244=80107=77393=77409.mp4
"""
import sys
import urllib
import urllib2
import requests
import os

def main():
    print len(sys.argv)
    if len(sys.argv) == 1:
        print "Usage: python videoDownload.py <flag> <value>\n\
                -u http://urllink\n\
                -f <file> with links of videos to download\n"
        sys.exit(0)

    if sys.argv[1] == "-u":
        url = sys.argv[2]
        name = url[url.rfind('/')+1:]
        urllib.urlretrieve(url,name)

        f =urllib2.urlopen(url)
        data = f.read()
        with open(name,'wb') as code:
            code.write(data)

        r = requests.get(url)
        with open(name,'wb') as code:
            code.write(r.content)
        os.system('/Applications/VLC.app/Contents/MacOS/VLC '+name)


    if sys.argv[1] == "-f":
        print sys.argv[2]
        textf= open(sys.argv[2],'r')

        for url in textf:
            #remove new line char
            url =url.strip('\n')

            #get name of file
            name = url[url.rfind('/')+1:]

            #remove newline char
            name = name.strip('\n')
            print 'Downloading: '+name
            urllib.urlretrieve(url,name)

            f =urllib2.urlopen(url)
            data = f.read()
            with open(name,'wb') as code:
                code.write(data)

            r = requests.get(url)
            with open(name,'wb') as code:
                code.write(r.content)
            code.close()


main()
