import os
dirs = os.listdir('/data')
if('cats' in dirs):
  print("Found Cats Datasets, Meow!")
else:
  print("No Cats Found :(")
