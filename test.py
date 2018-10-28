import random
import time


for i in range(100):
  print(f"test-{i}")
  with open(f"file-{random.randint(0,100)}.txt", "w") as f:
    f.write(f"hello123{random.randint(0,1000)}")
    f.write(f"hello123{random.randint(0,1000)}")
    f.write(f"hello123{random.randint(0,1000)}")
    f.write(f"hello123{random.randint(0,1000)}")
  time.sleep(5)
