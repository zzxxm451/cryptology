import paramiko
import time
import keyboard
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='192.168.0.1',username='user',password='huawei123',allow_agent=False,look_for_keys=False)
chan = client.invoke_shell()
chan.send(' \ndis cur\n')
chan.send('\nsystem \n')
info = chan.recv(99999).decode()
print(info)
while True:
    str_input = input()
    chan.send(' '+str_input+'\n')
    info = chan.recv(99999).decode()
    print(info)
    if str_input == "q":
        break
client.close()

