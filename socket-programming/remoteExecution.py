import winrm
sess = winrm.Session("laptop-6jvsdc18", auth = ('prana','1390'))
command = sess.run_cmd('ipconfig', ['/all'])
print(command.std_out)
