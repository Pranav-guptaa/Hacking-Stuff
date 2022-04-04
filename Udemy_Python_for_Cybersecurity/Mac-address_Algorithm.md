## MAC-Address changing algorithm
# LEC-1 subproces.check_output()
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


ifconfig_result = subprocess.chec_output(["ifconfig", options.interface])
print(ifconfig_result)
```

# LEC_2 regex function
# regex means regular expression and used for finding the text from a file or a string. This uses rules for performing the search
```python
import subprocess
import optparse
import re
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


ifconfig_result = subprocess.chec_output(["ifconfig", options.interface])
# print(ifconfig_result)

mac_add_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
if mac_add_search_result:
    print(mac_add_search_result.group(0))
else:
    print("[-] Could not read the MAC address")
# this prints the first result occured in the search
```


# REGEX CHEATSHEET
<!--  https://pythex.org/ -->
```bash
Special characters
\	escape special characters
.	matches any character
^	matches beginning of string
$	matches end of string
[5b-d]	matches any chars '5', 'b', 'c' or 'd'
[^a-c6]	matches any char except 'a', 'b', 'c' or '6'
R|S	matches either regex R or regex S
()	creates a capture group and indicates precedence
Quantifiers
*	0 or more (append ? for non-greedy)
+	1 or more (append ? for non-greedy)
?	0 or 1 (append ? for non-greedy)
{m}	exactly mm occurrences
{m, n}	from m to n. m defaults to 0, n to infinity
{m, n}?	from m to n, as few as possible
Special sequences
\A	start of string
\b	matches empty string at word boundary (between \w and \W)
\B	matches empty string not at word boundary
\d	digit
\D	non-digit
\s	whitespace: [ \t\n\r\f\v]
\S	non-whitespace
\w	alphanumeric: [0-9a-zA-Z_]
\W	non-alphanumeric
\Z	end of string
\g<id>	matches a previously defined group
Special sequences
(?iLmsux)	matches empty string, sets re.X flags
(?:...)	    non-capturing version of regular parentheses
(?P...)	    matches whatever matched previously named group
(?P=)	    digit
(?#...) 	a comment; ignored
(?=...)	    lookahead assertion: matches without consuming
(?!...)	    negative lookahead assertion
(?<=...)	lookbehind assertion: matches if preceded
(?<!...)	negative lookbehind assertion
(?(id)yes|no)match 'yes' if group 'id' matched, else 'no'

```

# LEC-5 

```python
import subprocess
import optparse
import re
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
def mac_address_searching(interface):
    ifconfig_result = subprocess.chec_output(["ifconfig", interface])
    mac_add_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_add_search_result:
        return mac_add_search_result.group(0)
    else:
        print("[-] Could not read the MAC address")
options = get_arguments()
current_mac = mac_address_searching(options.interface)
change_mac(options.interface, options.new_mac)
current_mac = mac_address_searching(options.interface)


if current_mac == options.new_mac:
    print("SAME")
else:
    print("NOT SAME")