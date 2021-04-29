#!/usr/bin/python3
import sys
r=input()
print("Value fed using input is ",r)


for i in sys.stdin:
    if i == 'q\n':
        break
    print(i.rstrip())