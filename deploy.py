import random



def is_it_dog(dog):
  sol = "not " if random.choice([True, False]) else ""
  print(dog + " is " + sol + "a dog name")
