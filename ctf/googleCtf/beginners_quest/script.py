offest = 0xcafe

password = {0:52037, 6:52081, 5:52063 ,1:52077 ,9:52077 ,10:52080, 4:52046 ,3:52066 ,8:52085 ,7:52081 ,2:52077 ,11:52066}

output = ""

for i in range(12):
    output += chr(password[i]-offest) # here it is just subtracting the values of dictionary with the offset 
print(output)


