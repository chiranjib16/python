import re , subprocess
#ip = raw_input("provide an ip address:")
p1 = subprocess.Popen(['ping','8.8.8.8'], stdout = subprocess.PIPE)
output = p1.communicate()[0]
aa = re.search(r"\d+.\d+.\d+.\d+",output)
print output
if aa:
    print aa.group()
    val = aa.group()
    print val

temp =  val.split(".")
print temp
temp = map(int,temp)

print temp

temp[3]=temp[3]+1

print temp