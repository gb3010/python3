#!/usr/bin/python3

import os 

g=os.fork()

if g == 0:
    print("pid of child process is ",os.getpid())
else:
    print("pid of parent process is ",os.getpid())