import subprocess
import parser

# bashCmd = ["ls", "."]
subprocess.call('ls -la', shell=True)
subprocess.call('echo $HOME', shell=True)
subprocess.call('mkdir hello',shell=True)


'''
another = subprocess.Popen(new_bash, stdout=subprocess.PIPE)
another_output, error = another.communicate()
print(another_output)
print()
process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)
'''
