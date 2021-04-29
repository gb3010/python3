#!/usr/bin/python3
import sys

for line in sys.stdin:
    if line.rstrip() == 'q':
        break
    print(line)


