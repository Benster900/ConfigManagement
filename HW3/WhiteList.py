"""
Author: Ben Bornholm
Date: 9-9-15
Desription: Use a list of regular expression to parse log files
"""

import re

def main():
    #Regex list
    parseList = ['APPCRASH', 'he protected system file',
                'EMET_DLL Module logged the following event:',
                'your virus/spyware' ,'A new process has been created',
                'A service was installed in the system',
                'A scheduled task was created','Logon Type:',
                '\\\Software\\\Microsoft\\\Windows\\\CurrentVersion\\\Run',
                "service terminated unexpectedly",'service was successfully sent a',
                'service entered the', 'service was changed from' ]

    #Files containing data to parse
    f1 = open('WindowsSystemEvents.csv','r')
    f2 = open('WindowsApplicationEvent.csv','r')

    x = 0
    for line in f1:
        for pattern in parseList:
            if pattern in line:
                x=x+1
                print line


    for line in f2:
        for pattern in parseList:
            if pattern in line:
                x=x+1
                print line

    print x

main()
