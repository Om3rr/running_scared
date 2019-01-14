import random
import time
import os
if(not os.path.isdir('output')):
  os.mkdir('output')
  
 
for i in range(1000):
  n = random.randint(0,10000)
  f = open("output/new-file-%s"%n, "w+")
  f.write("Wowwwwww")
  f.write("%s"%n)
  print("File Created!!!! n=%s"%n) 
  time.sleep(20)
