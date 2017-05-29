import subprocess

host = raw_input("enter the host name:")

p1 = subprocess.Popen(['ping',host],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)


output = p1.communicate()[0]

print output
