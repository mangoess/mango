import os
import socket
import subprocess
print (socket.gethostbyname(socket.gethostname()))
ip = (socket.gethostbyname(socket.gethostname()))


data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))
input("")

#subprocess = subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE)
# ^^^^^^ Store specific output from cmd


#import subprocess
#s = 5
#cmd = ['stress', '-c', '5', '-i', '1', '-m', '1',
#      '--vm-bytes', '128M', '-t', str(s)]
#subprocess.call(cmd)
# Should let me use variables in shell