#!/usr/bin/python3

print("Enter the string");
InputString = input();
ListofChar = [];
SetofChar = {};
for i in InputString:
    ListofChar.append(i);

SetofChar = set(ListofChar);

if len(SetofChar) == 1:
    print("All characters in {x} is unique".format(x=InputString))
