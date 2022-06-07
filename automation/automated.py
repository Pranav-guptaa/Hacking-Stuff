import subprocess
import argparse

# subprocess.call('ls -la', shell=True)
# subprocess.call('echo $HOME', shell=True)
# subprocess.call('mkdir hello',shell=True)
parser = argparse.ArgumentParser()

parser.add_argument("operations",help="operation")
parser.add_argument("suboperation",help="sub operation")
parser.add_argument("--url",help = "url")
parser.add_argument("--list",help = "wordlist")
parser.add_argument("--ip",help="Ip address")
def main():
	if args.operations == 'nmap':
		subprocess.call('mkdir nmap',shell=True)
		if args.suboperation == 'def':
			subprocess.call('nmap -sC -sV -oA nmap/initial'+args.ip,shell=True)
		elif args.suboperation == 'ver':
			subprocess.call('nmap -sV '+args.ip,shell=True)
		elif args.suboperation == 'syn':
			subprocess.call('nmap -sS '+args.ip,shell=True)
		else:
			print("Enter a valid option.")
			subprocess.call('python3 automated.py -h',shell=True)
	elif args.operations == 'la':
		subprocess.call('ls -la',shell=True)
	elif args.operations == 'ping':
		subprocess.call('ping -c3 '+args.ip,shell=True) 
	elif args.operations == 'gobust':
		if args.suboperation == 'dir':		
			# url = args.url
			# wordlist = args.wordlist
			subprocess.call('gobuster dir -u '+ args.url +' -w '+args.list+ ' -o bruteforce.txt',shell=True)
		else:
			print("Enter a valid option.")
			subprocess.call('python3 automated.py -h',shell=True)
args = parser.parse_args()

main()
# elif args.operations == 'msfconsole':
# 	subprocess.call('msfconsole',shell=True)
# 	if args.suboperation == 'se':
# 		# object = args.suboperation


'''	
parser.add_argument("Num1",help = "Enter the first number") # these are mandatory or positonal arguments
parser.add_argument("Num2", help="Enter the second number") 
parser.add_argument("operation",help="operation to be perfomed") 

# but if we add '--' infront of the argument name then it become optional
# for example:
# parser.add_argument("--operation",help="operation to be perfomed")
# now operations become an optional argument

n1 = int(args.Num1)
n2 = int(args.Num2)
# print(args.Num1)
# print(args.Num2)
# print(args.operation)

if args.operation == 'add':
	result = n1+n2
	# return result
elif args.operation == 'sub':
	result = n1 -n2
elif args.operation == 'mul':
	result = n1*n2
print(result)

'''