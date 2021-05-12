#!/usr/bin/python3

import os

f=os.fork()

if f:
    p=os.wait()
    print(p)
