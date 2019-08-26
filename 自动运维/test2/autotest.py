import paramiko
import os,sys,time,select

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect("192.168.10.10", 22, "root", "126.com")

#stdin, stdout, stderr = ssh.exec_command("ip a")
#print(stdout.read().decode())

tran = paramiko.Transport("192.168.10.10",22)
tran.start_client()
tran.auth_password('root', "126.com")
chan = tran.open_session()
chan.settimeout(10)
chan.get_pty()
chan.invoke_shell()
chan.send("ls")

print(chan.recv(65535).decode())

tran.close()
