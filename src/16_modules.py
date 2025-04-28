import  time
import datetime
import sys, os, platform
import  math
from math import floor #importing one function from library
import own_module

a = time.time()
print(a)
time.sleep(1)
print(time.time() - a, "_ sec passed")

s = datetime.datetime.now().time()
d = datetime.datetime.now().date()
print(s, d)

print(sys.path)
print(os.name)
print(os.listdir("/"))
print(platform.system())
print(platform.version())

print(math.sqrt(4))
print(math.ceil(14.34)) # round to higher value
print(floor(14.94)) #round to lower value

print(own_module.alex)
print(own_module.add_3_numbers(1, 4, 4.5))
own_module.hi()