# Meow Machine
## Enumeration and Foothold:
    1. port scanning (nmap)
    2. research to be done over internet
    3. after a successful vpn connection try pinging the device with its ip 
    4. go for the nmap scan with -sV flag so as to get the name and the services with their versions running on particular port
       sudo nmap -sV {target-ip}
    5. telnet service runs on port number------> 23/tcp
       and as the target is running this service this means that we can connect to the target as:
       telnet {target-ip}
    6. after a successful connection we need find the login credentials
       and for this we might try higher post usernames like:::: admin, administrator and root 
       even these types of machines are left vulnerable with just very easily crackable passwords and even sometimes with no password

    7. after the root credentials get validated and after logging into the machine just list the directory and hence after opening the
       'flag.txt' you will get the flag and 

Congrats!!!!!
