# Fawn machine

## File trandfer protocol

  1. it is used for transferring files from a server to the client
  2. this works on client-server model
  3. in this the authentication is done with clear texts until its configured to do so 
  4. it is secured using SSL/TLS (FTPS) or replaced with SFTP(SSH File Transfer Protocol)
  5. FTP service is also available in GUI mod. For example: FileZilla
  6. FTP port number: 21/tcp 
Important ----> SSH at port 22{Secure Shell Protocol} is also a service which is available and 
                HTTPD at port 80(Web server)

## Enumeration: 
  1. this includes ping and nmap scan 

## Foothold:
  1. after a successful nmap scan we got to know that the machine is vulnerable at port number: 21(ftp)
  2. so to exploit this we will run ftp connection command 
  3. if ftp doesn't exists then 'sudo apt install ftp -y' and then "ftp {target-ip}"
  4. now comes the login page and due to misconfiguration in ftp server it allows "anonymous" login and hitting enter in
     front of password will lead to a successfull login i.e. username: anonymous password: {just-press-enter}
  5. now after logging into the server type help and read about the various commands.
  6. now "ls" into the directory and after getting 'flag.txt' file just fire the command: 'get flag.txt'
  7. this file will be saved in the current directory you are working in your system.
  8. for exiting the server just type: exit or bye
  9. Now list your current directory and submit the flag.

CONGRATS!!!!!
