import os
dirs = os.listdir("/data/")
if("dogs" in dirs):
  print("Whoof whoof found some dogs")
else:
  print("Didnt find any dog :( ")
