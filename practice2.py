import subprocess
import re
host = raw_input("enter an ip address:")

p2 = subprocess.Popen(['ping',host],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

for line in p2.stdout.readlines():
 #   pattern = re.search(r'bytes',line,re.M)
    print line
 #   if(pattern):
  #      print pattern.group(1)

