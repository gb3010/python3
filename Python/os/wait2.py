#!/usr/bin/python3

import os

f=os.fork()
#print(type(f))
#print(f)

# if f == 0:
#   print("Executing from child process")
# else:
#   print("Executing from parent process")

if f == 0:
  print("value of f is ",f)
  print("This is Child process")
else:
  print("Value of  f is ",f)
  print("This is parent process")