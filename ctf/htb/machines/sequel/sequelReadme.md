# Sequel Machine 
## Introduction:
  1. this machine is focused on the concept of sql database
  2. and even most of the critical data is stored in this database such as passwords and usernames.
  3. many companies uses databases such as MySQL and MariaDB because these store the accumalted data at places which are easily accessible.
  4. this data could include usernames and passwords also.
  5. post-login the web application will assign a special permission in the form of cookies or authentication token to authenticate the 
     persence on a website.
  6. these cookies are stored both locally, on the user's browser storage and the webserver.


## Enumeration:
  1. nmap scan found 3306/tcp port with MySQL service running on it.

## Foothold:
  1. so as we have the option of MySQL then we will first install it using::: sudo apt install mysql
  2. then run:: mysql --help
  3. mysql -h {target-ip} -u root ------> -h: connects to the host, -u: user login, root: this doesn't require any credentials so
     we logined as root.
  4. Most essential commands are as follows:
      
      SHOW databases;              : Prints out the databases we can access.
      USE {database_name};         : Set to use the database named {database_name}.
      SHOW tables;                 : Prints out the available tables inside the current database.
      SELECT * FROM {table_name};  : Prints out all the data from the table {table_name}.
  5. According to the above mentioned commands we will use:::
      show databases;
      use htb;
      show tables;
      select * from config;
  6. and hence you will find the flag.

CONGRATS!!!!!
