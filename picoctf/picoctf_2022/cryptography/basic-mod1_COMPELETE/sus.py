file = open('message.txt','r')
data = file.read()
# data = [(i%37) for i in range(len(data))]
new_data= []
j=0
for i in range(len(data)-1):
    if i!=" ":
        new_data[j]+= str(i)
    else:
        j = j+1
print(new_data)
