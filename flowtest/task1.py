import os
import random
if not os.path.exists('output'):
  os.mkdir('output')
f = open('output/testFile', 'w')
token = random.randint(0,10000)
f.write("I was created with task1 %s"%token)
f.close()
print("cnvrg_tag_token %s"%token)
