# MAC ADDRESS
```
Media access control
    its permanent
        physical 
        Unique
    Assigned by the manufacturer
```
# WHY CHANGE IT
```bash
increase anonymity
impersonate other devices
bypass filters
```

# CHANGING IT MANUALLY
```bash
ifconfig
interface: this is connected

# ifconfig <interface-name> down
    ifconfig interface down
    to disable the interface

# Changing MAC address
ifconfig <interface-name> hw ether <MAC-address-random>
ifconfig interface hw ether 00:11:22:33:44:55
this changed the MAC address

ifconfig interface up
to enable the interface

ifconfig
the ether part got changed.
```
# CHANGING MAC ADDRESS USING PYTHON
```python 
import subprocess

subprocess.call("ifconfig",shell=True)
subprocess.call("ifconfig interface down",shell=True)
subprocess.call("ifconfig interface hw ether 00:11:22:33:44:66",shell=True)
subprocess.call("ifconfig interface up",shell=True)
```

```python 2
import subprocess
interface = raw_input()
mac_address = raw_input()
subprocess.call("ifconfig",shell=True)
subprocess.call("ifconfig"+ interface +" down",shell=True)
subprocess.call("ifconfig"+ interface +"hw ether" +mac_address ,shell=True)
subprocess.call("ifconfig interface up",shell=True)



input = wlan0;ls;
# this will execute any type of command in the linux system as there is no constraint applied on the input

# as a result it first execute the wlan0 command and then the ls command.

# so this code is vulnerable

# lets fix this code then
```

# FIXING THE CODE
``` python

import subprocess
interface = input()
mac_address = input()
subprocess.call(["ifconfig",interface, "down"])
subprocess.call(["ifconfig",interface,"hw", "ether",mac_address,"down"])
subprocess.call(["ifconfig",interface, "up"])
# this is a more secure than above one
```
# optparse: taking the input from the user using command line arguments.

```python
import subprocess
import optparse

parser = optparse.OptionParser()
# object created of optionParser class
parser.add_option("-i","--inteface",dest="interface",help='interface to change its mac address')
parser.add_option("-m","--mac",dest="new_mac",help='new mac address the person wants to use')
(options, arguments) = parser.parse_args() 
# helps the program to understand what the user has entered and returns the arguments and values entered by the user in the variables calles options and arguments respectively.
# options will contain the values i.e. are wlan0 or eth0 and the arguments will contain --i and --m
# to access the values stored in the options tag we use
#     options.interface and options.new_mac
# i.e. options.destination_name


# the above line sets options i.e. -i or --interface and stores the value in interface 
interface = options.interface
mac_address = options.new_mac
subprocess.call(["ifconfig",interface, "down"])
subprocess.call(["ifconfig",interface,"hw", "ether",mac_address,"down"])
subprocess.call(["ifconfig",interface, "up"])
# hence we were able to change the mac address successfully
```



# functions

```python
import subprocess
import optparse
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--inteface",dest="interface",help='interface to change its mac address')
    parser.add_option("-m","--mac",dest="new_mac",help='new mac address the person wants to use')
    return parser.parse_args()
    
def change_mac(interface,new_mac):
    subprocess.call(["ifconfig",interface, "down"])
    subprocess.call(["ifconfig",interface,"hw", "ether",mac_address,"down"])
    subprocess.call(["ifconfig",interface, "up"])

(options, arguments) = get_arguments()
# this statement makes the options and arguments accessible for the function below by returning the values to options and arguments.
change_mac(interface, mac_address)
```

# decision making
```python
import subprocess
import optparse
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--inteface",dest="interface",help='interface to change its mac address')
    parser.add_option("-m","--mac",dest="new_mac",help='new mac address the person wants to use')
    (options,arguments) = parser.parse_args()
    if not options.interface:
        # code to exception error.
        parser.error("Please a interface)
    elif not options.new_mac:
        parser.error("Please a mac address)
        # code to handle error
    return options


def change_mac(interface,new_mac):
    subprocess.call(["ifconfig",interface, "down"])
    subprocess.call(["ifconfig",interface,"hw", "ether",mac_address,"down"])
    subprocess.call(["ifconfig",interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)
```