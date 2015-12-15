"""
Author: Ben Bornholm
Date: 8-31-15
SMTP Sever: smtp-server.rit.edu
"""
import sys
import re
import smtplib

def main():
    #chck command line arguments
    if(len(sys.argv) != 3):
        print "Please use python failscan.py [file to read] [e-mail]"
        sys.exit()

    #open file
    f = open(sys.argv[1],'r')

    #Create a file
    firstline = f.readline() #read first line
    date = re.search(r'\d\d\d\d-\d\d-\d\d', firstline) #get date from regex
    date = date.group()
    year, month, day = date.split('-') #split date into various vars
    output = open("logfile_scan."+month+day+year,'w')#(month, day, year) #create file based on date vars

    #Write line number
    output.write("Received Date format from the first line")

    counter =0
    for row in f:
        if "fail" in row:
            output.write(row)

    message = ""
    for row in open("logfile_scan."+month+day+year,'r'):
        message += row + '\n'


    #Send e-mail
    sender = 'nope@me.com'
    receiver = 'benster900@gmail.com'

    smtpObj = smtplib.SMTP('smtp-server.rit.edu')
    smtpObj.sendmail(sender, receiver, message)
    print "Successfully sent email to "+ receiver





main()
