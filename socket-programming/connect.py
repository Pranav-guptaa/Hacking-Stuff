import os
from socket import *
import wmi
import win32com
'''
# file = open("Try.txt")
file = open("D:\\Pycharm Projects\\Minor project\\CompleteBodyDetector.py")
count = 0

for line in file:
    count = count + 1
    # print(line)
print("Line count: ", count)

'''


def remote_connection():
    ip = '192.168.43.155'
    username = 'prana'
    password = '1390'
    try:
        print("Establishing connection to %s" % ip)
        connection = wmi.WMI(ip, user=username, password=password)
        print("Connection established")
    except wmi.x_wmi:
        print("Your Username and Password of " + getfqdn(ip) + " are wrong.")


def applications_opening(num):
    if num == 0:
        os.system("start .")
    elif num == 1:
        os.system("Notepad")
    elif num == 2:
        os.system("cmd")


if __name__ == '__main__':
    # choice = int(input("shell%> "))
    # applications_opening(choice)
    remote_connection()
