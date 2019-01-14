import random



def is_it_dog(dog):
  sol = "not " if random.choice([True, False]) else ""
  return dog + " is " + sol + "a dog name"
