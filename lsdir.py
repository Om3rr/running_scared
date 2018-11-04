import os
import random
if 'output' in os.listdir('.'):
  print(os.listdir('output'))
  f = open('output/test', 'w+')
  f.write("the number is: %s"%random.randint(0,1000))
else:
  print("Output dir is empty.")
  os.mkdir('output')
  f = open('output/test', 'w+')
  f.write("the number is: %s"%random.randint(0,1000))
