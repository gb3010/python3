#!/usr/bin/python3

import sys
print("Enter the arg to append")
pattern=input().strip()
for i in sys.stdin:
    if i.rstrip() == 'done':
        break
    #sys.stdout.write(i,pattern)
    #sys.stdout.flush()
    print(i+'-'+pattern)