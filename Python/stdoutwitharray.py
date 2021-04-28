#!/usr/bin/python3
import sys
arr=['new','file','text']


for i in arr:
    sys.stdout.write(i)  #Does not append newline

sys.stdout.write('\n') #Writing newline for readability

for i in arr:
    sys.stdout.write(i+'\n') #Adding newline since sys stdout does not append newline 