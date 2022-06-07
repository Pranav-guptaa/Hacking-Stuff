## Appointment Machine
# Introduction:
  1. its a web-application based machine
  2. its a sql injection vulnerable machine
  3. the websites mainly use databases such as: MySQL and MariaBD because the data they collect needs to be stored somewhere.
  4. this data coulf be usernames,passwords and sensitive sets such as PII{Personally Indentifiable Information}
  5. if the company disregards towards protecting a user's PII then it has pay a large amount of fine for this 
  6. to overcome sql injection vulnerability:: input validation, parameterized queries, stored procedures and implementation of 
     WAF{Web Application Firewall}


# Enumeration:
  1. nmap scan to be performed and the port we detected is 80 and this runs an Apache httpd server
  2. Apache httpd server is a free and open-source application that runs web pages.
  3. this service usually runs on ports:: 80 TCP and 443 TCP and even on 8080,8000 TCP.
  4. HTTP is a application layer protocol used for transferring hpermedia documents such as HTML.
  5. while visiting various directories in a website:
            if(a directory is a valid one):
                  Response code::: 200 {OK} 
            else:
                  Response code::: 404 {Not found} 
  6. for making the enumeration process automate various tools are Gobuster, Dirbuster and Dirb, many more and these are known as 
     brute-forcing tools.

# Gobuster installation{{In Parrot its aleready installed}}:
----> Understanding about GO lannguage:
        1. Go is a statically types, compiled languge designed by Google.
        2. it syntactically similar to C but with memory safety, garbage collection, CSP-style concurrency and structural typing.
        3. often reffered as Golang because of its domain name: golang.org
        4. Fast compilation and many more.

----> Installation of Gobuster:
        1. go install github.com/OJ/gobuster/v3@latest
        2. git clone https://github.com/OJ/gobuster.git
        3. then navigate to the gobuster folder and then fire the below command:
        4. go get && go build
        5. go install
     Now you have finally installed Gobuster.


# Brute-forcing directories:
  1. Download the Seclists by this command::: git clone https://github.com/danielmiessler/SecLists.git
  2. gobuster dir -u {target-url} -w {wordlist-directory}
  3. After performing this step we could not found anything useful so lets move on to next step


# Foothold:
  1. We will now try logging into the accounts such as:
        admin:admin
        guest:guest
        user:user
        root:root
        administrator:password
     But still we didn't found anything useful.
  2. So now we will test for SQL injection vulnerabilty.
  3. So Now we see something interesting:
          Here is an example of how authentication works using PHP & SQL:
				<?php
					mysql_connect("localhost", "db_username", "db_password"); # Connection to the SQL
					Database.
					mysql_select_db("users"); # Database table where user information is stored.
					$username=$_POST['username']; # User-specified username.
					$password=$_POST['password']; #User-specified password.
					$sql="SELECT * FROM users WHERE username='$username' AND password='$password'";
					# Query for user/pass retrieval from the DB.
					$result=mysql_query($sql);
					# Performs query stored in $sql and stores it in $result.
					$count=mysql_num_rows($result);
					# Sets the $count variable to the number of rows stored in $result.
					if ($count==1){
					# Checks if there's at least 1 result, and if yes:
					$_SESSION['username'] = $username; # Creates a session with the specified $username.
					$_SESSION['password'] = $password; # Creates a session with the specified $password.
					header("location:home.php"); # Redirect to homepage.}
					else { # If there's no singular result of a user/pass combination:
					header("location:login.php");
					# No redirection, as the login failed in the case the $count variable is not equal to
					1, HTTP Response code 200 OK.
					}
				?>  
  4. Notice how after the # symbol, everything turns into comments and this is how php works and this thing needs 
     to be kept in mind.
  5. And therefore this code is vulnerable to SQL injection so we will try a payload as ::: admin'# 
  6. the abpve mentioned paylod tells the sql query that if there is a user as admin then just let him in 
     without any password because:
            QUERY---> insert into login table where username= 'admin'#' and password='a'
            ***So in the the query after the username authentication got commented and therefore we were able to sign in ***
            ***and here password can be anything because after "#" everything got commented so no verification is going to be carried out***\
  7. After a successful login we will get a flag and Submit it.

CONGRATS!!!!!

            standard port used for the HTTPS protocol? 
