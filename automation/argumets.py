import subprocess
import argparse

# subprocess.call('ls -la', shell=True)
# subprocess.call('echo $HOME', shell=True)
# subprocess.call('mkdir hello',shell=True)
parser = argparse.ArgumentParser()

parser.add_argument("ip",help="Ip address")
parser.add_argument("operations",help="operation")
args = parser.parse_args()

if args.operations == 'nmap':
	subprocess.call('mkdir nmap',shell=True)
	subprocess.call('nmap -sC -sV -oA nmap/initial'+args.ip,shell=True)
elif args.operations == 'la':
	subprocess.call('ls -la',shell=True)
else:
	help 
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