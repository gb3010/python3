#!/usr/bin/python3

from signal import *
import time

signal(SIGINT,SIG_IGN)

for i in range(1,10):
    print(i)
    time.sleep(1)