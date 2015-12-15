"""
Author: Ben Bornholm
Date: 10-30-15
Description: Write a script to install and start xamp on a remote machine. Use your virtual network. Use one machine to run
the script and the other machine to receive the install.

"""
import os
import sys
import paramiko

def main():
    if len(sys.argv) != 3:
        print "Usage python sshRunner.sh -f <file>"
        sys.exit()

    remoteServer= str(raw_input("Please enter IP address of remote server: "))
    #remotePort = str(raw_input("Please enter port for remote server: "))
    #remoteUser = str(raw_input("Please enter a username for remote server: "))
    #remotePass = str(raw_input("Please enter a password for remote server: "))

    #connect to server
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(remoteServer,username='root',password='password123')

    f = open(sys.argv[2],'r')
    for line in f:
        if '#' not in line:
            stdin,stdout,stderr = ssh.exec_command(line)

            print("Reading outputs from the remote server")
            for l in stdout:
                print("stdout: %s" % l.strip())

            for l in stderr:
                print("stderr: %s " % l.strip())

    #Close file
    f.close()
    ssh.close()

main()
