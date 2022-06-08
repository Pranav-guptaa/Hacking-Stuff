#!/usr/bin/env python3
'''
with open('message.txt') as filp:
    contents = filp.read()
    strings = contents.split()
    
    for every_value in strings:
        print(int(every_value))'''
import string
flag =[]
with open('message.txt') as filp:
    contents = filp.read()
    numbers = [int(val) for val in contents.split()]
    # print(numbers)

    for number in numbers:
        modulus = number % 37
        if modulus in range(26):
            # print(string.ascii_uppercase[modulus], end="") 
            flag.append(string.ascii_uppercase[modulus])
        
        elif modulus in range(26, 36):
            # print(string.digits[modulus-26], end="")
            flag.append(string.digits[modulus-26])
        
        else:
            # print("_", end="")
            flag.append("_")
print("picoCTF{%s}" % "".join(flag))
# print(string.ascii_uppercase[0])

# print(string.digits)