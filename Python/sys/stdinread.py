#!/usr/bin/python3
import sys

r=sys.stdin.read()

# sys.stdout.write(r)

# for i in r:
#     sys.stdout.write(i+'-'+'world')


sys.stdout.write(r+'-'+'world')

# Node: read() does not delimit the input using newline. Instead each character is considered a single element when iterated through loop.