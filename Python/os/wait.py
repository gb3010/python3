#!/usr/bin/python3

import os

f=os.fork()
print(f)

if f:
    p=os.wait()
    print(p)
