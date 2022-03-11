#!/usr/bin/python3
import os

def solve(s):
    listofstring = s.split()
    numberofwords = len(listofstring)
    
    for i in range(numberofwords):
        if listofstring[i][0].isalpha():
            listofstring[i] = listofstring[i].title()
    
    finalstring = ' '.join(listofstring)
    return finalstring

if __name__ == '__main__':

	s = input()
	result = solve(s)
	print(result)


