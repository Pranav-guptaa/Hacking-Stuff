# Intelligence machine

nmap scan done and found various ports open

80/tcp   open  http          Microsoft IIS httpd 10.0
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-06-08 20:14:45Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP

The ldap leaks a domain called: dc.intelligence.htb 
add it into hosts file: sudo vim /etc/hosts
 
10.129.169.42	dc.intelligence.htb intelligence.htb intelligence

Then we tried out:
---> rpcclient -U '' 10.129.169.42
---> rpcclient -U '' -N 10.129.169.42                                                                                            
---> crackmapexec smb 10.129.169.42
---> crackmapexec smb 10.129.169.42 --shares
---> crackmapexec smb 10.129.169.42 --pass-pol
---> crackmapexec smb 10.129.169.42 --users

But here shares command was giving an error lets try it out again
---> crackmapexec smb 10.129.169.42 -u '' -p '' --shares
here we get to know that passwords if specified if not has a difference

But nothing worked so lets visit the website: 10.129.169.42

After enumering the site we get some pdfs with their names as date-upload.pdf 
so now lets enumerate it further by making our own wordlist for directory bruteforcing using date command

date
date --date="1 day ago" 
date --date="1 day ago" +%Y-%m-%d-upload.pdf
date --date="520 day ago" +%Y-%m-%d-upload.pdf

for i in $(seq 520 885); do date --date="$i day ago" +%Y-%m-%d-upload.pdf; done > files.txt> 

curl http://10.129.169.42/documents/2020-12-15-upload.pdf -o test.pdf

<!-- OR -->

wget http://10.129.169.42/documents/2020-12-15-upload.pdf

<!-- OR -->

curl -R http://10.129.169.42/documents/2020-12-15-upload.pdf -o test.pdf

The above command preserves the time stamp of the files
sudo apt install exiftool

exiftool 2020-12-15-upload.pdf


http://10.129.169.42/documents/2020-12-15-upload.pdf

<!-- machine is not solved -->