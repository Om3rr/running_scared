import os
if not os.path.exists('output/testFile'):
  print("ERRROR")
  exit(1)
f = open('output/testFile', 'r')
print("Found token!! %s"%f.read())
