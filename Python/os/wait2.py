#!/usr/bin/python3

import os

f=os.fork()
print(f)

if f == 0:
  print("Executing from child process")
else:
  print("Executing from parent process")

