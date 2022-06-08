import string
flag = list()
with open('message.txt') as f:
    contents = f.read()
    numbers = [int(val) for val in contents.split()]

    for number in numbers:
        # modulus=number%41
        '''
        To calculate the modulo multiplicative inverse using the pow()
        method, the first parameter to the pow() method will be the 
        number whose modulo inverse is to be found, the second
        parameter will be the order of modulo subtracted
        by 2 and the last parameter will be the order of modulo. 
        '''
        modulus = pow(number,-1,41)

        if modulus in range(1,27):
            flag.append(string.ascii_uppercase[modulus-1])

        elif modulus in range(27,37):
            flag.append(string.digits[modulus-27])
        
        else:
            flag.append("_")
print("picoCTF{"+"".join(flag)+"}")

