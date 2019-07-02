import subprocess

p=subprocess.Popen("bash", shell=True, stdout=subprocess.PIPE)
out=p.stdout.readlines()

for line in out:
    print(line)