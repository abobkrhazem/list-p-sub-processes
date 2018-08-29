import subprocess
command = subprocess.Popen('ls', stdin=subprocess.PIPE, stderr=subprocess.PIPE)
print(command)
