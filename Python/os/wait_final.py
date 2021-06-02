#!/usr/bin/python3

import os

f = os.fork() 

if f == 0:
    print("We are in child process with pid %d" % os.getpid())

    for i in range(5):
        print("Printing ",i)
else:
    print("Parent process with "+str(os.getpid())+" is waiting")
    p = os.wait()
    print("Child process %d exited " % p[0])
    print("Parent process %d exiting after child" % os.getpid())
    # print(p)