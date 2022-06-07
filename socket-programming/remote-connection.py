#!/usr/bin/env python

import wmi
import os
import subprocess
import re
import socket, sys

def main():
     host="remotemachine"
     username="adminaam"
     password="passpass!"
     server =connects(host, username, password)
     s = socket.socket()
     s.settimeout(5)
     print server.run_remote('hostname')

class connects:

    def __init__(self, host, username, password, s = socket.socket()):
        self.host=host
        self.username=username
        self.password=password
        self.s=s

        try:
            self.connection= wmi.WMI(self.host, user=self.username, password=self.password)
            self.s.connect(('10.10.10.3', 25))
            print "Connection established"
        except:
            print "Could not connect to machine"


   def run_remote(self, cmd, async=False, minimized=True):
       call=subprocess.check_output(cmd, shell=True,stderr=subprocess.STDOUT )
       print call

main() 
