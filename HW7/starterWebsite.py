"""
Author: Ben Bornholm
Date: 9-23-15
Description: Write a script that will create the "starter" website for a new user. The root folder for
the user's website will be the user's username. Your script must place the user's website within either
an apache webserve or an ISS webserver.
"""

import os
import shutil

def main():
    username = str(raw_input("Enter your username: "))
    domainname = str(raw_input("Enter domain name for website: "))
    webserver = str(raw_input("Enter the type of webserver(Apache or IIS): "))

    #If apcahe webserver is selected to be used
    if webserver == "apache":
	#Create #index.html file
    	if not os.path.exists('/var/www/html/'+username):
		os.makedirs('/var/www/html/'+username)
		os.makedirs('/var/www/html/'+username+'/pictures')
		os.makedirs('/var/www/html/'+username+'/database')
		os.makedirs('/var/www/html/'+username+'/mail')
	htmlFile = open('/var/www/html/'+username+'/index.html','w')
        message = "<html>\
                    <p><b>Welcome %s to %s</b></p>\
                </html>"%(username,domainname)

        #Write code for website
        htmlFile.write(message)

	#create dns redirect
	with open('/etc/hosts','a') as myfile:
		myfile.write('127.0.0.1\t'+domainname)
	os.system('sudo /etc/init.d/networking restart')

	#Create DNS records
	os.system('python ~/Desktop/dnsRecord.py '+domainname)
	
	#print website
	print "http://%s/%s/index.html"%(domainname,username)
    #If IIS webserver is selected to be used
    else:
        if not os.path.exists('/var/www/html/'+username):
		os.makedirs('/var/www/html/'+username)
	htmlFile = open('C:\inetpub\wwwroot\\'+username+'\\'+username+'.html','w')
        message = "<html>\
                    <p><b>Welcome %s to %s</b></p>\
                </html>"%(username,domainname)

        #Write code for website
        htmlFile.write(message)

main()
