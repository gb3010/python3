#!/usr/bin/python3
import sys

p=input()
print("Entered pattern is ",p)
r=sys.stdin.readlines()

for i in r:
    sys.stdout.write(i.rstrip()+'-'+p+'\n')


'''
sys.stdin is a class. Assigning it to a variable does not help
sys.stdin.readlines() expects multi line input with newline as delimiter
sys.stdin.readline() expects single line input with newline as delimiter  
'''