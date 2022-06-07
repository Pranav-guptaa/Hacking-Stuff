import socket
import sys

try:
	sock = socket.socket(sock.AF_INET, sock.SOCK_STREAM)

except socket.error as err:
	print("Failed to create a socket")
	print("Reason "+ str(err))
	sys.exit()
print("socket created")
#s = socket.socket(family = AF_INET, type = SOCK_STREAM, port=0)

target_host = input("ENter the target_host: ")
target_port = input("Enter the target_port: ")

try:
	# global sock
	sock.connect(target_host,int(target_port))
	print("socket connected to: "+str(target_host)+ str(target_port)
	sock.shutdown(2)     
except socket.error as err:
	print("Failed to connect"+ target_host+" "+ target_port)
	print("Reason"+str(err))
	sys.exit()
	
