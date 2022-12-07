#!/usr/bin/python
###############################################################################
# There is no hope
#
###############################################################################

from hashlib import sha256
from base64 import b64encode, b64decode
from subprocess import Popen, call, PIPE
from time import sleep
import urllib2
from datetime import datetime

    
def checkVPN():
    online = False
    
    for run in range(0, 2):
        proc = Popen('ps aux | grep openvpn | grep -v grep', stdout=PIPE, stderr=PIPE, shell=True)
        stdout_value = proc.stdout.read()
        
        if not "openvpn" in stdout_value:
            logging(str(datetime.now()) + " openvpn not running, restarting openvpn")
            Popen('/etc/init.d/openvpn start', stdout=PIPE, stderr=PIPE, shell=True).wait()
        else:
            proc = Popen('ping -c 1 192.2.0.6', stdout=PIPE, stderr=PIPE, shell=True)
            stdout_value = proc.stdout.read()
            if "bytes from" in stdout_value:
                online = True
                break
            else:
                logging(str(datetime.now()) + " openvpn gw not reachable, restarting openvpn")
                Popen('/etc/init.d/openvpn restart', stdout=PIPE, stderr=PIPE, shell=True).wait()
                
        sleep(3)
                
    return online

def logging(l):
    f = open("/home/kali/device_status.log", "a")
    f.write(l)
    f.write("\n")
    f.close()

# Main
logging(str(datetime.now()) + " Waiting 30 seconds for boot")
sleep(30)
logging(str(datetime.now()) + " checking VPN")

if(checkVPN()):
    logging(str(datetime.now()) + " Sending notify message: active")
    proc = Popen('bash /var/scripts/hilink.sh active', stdout=PIPE, stderr=PIPE, shell=True)
    stdout_value = proc.stdout.read()
else:
    proc = Popen('bash /var/scripts/hilink.sh inactive', stdout=PIPE, stderr=PIPE, shell=True)
    logging(str(datetime.now()) + " Sending notify message: inactive")
    stdout_value = proc.stdout.read()   
