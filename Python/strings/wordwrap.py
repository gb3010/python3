#!/usr/bin/python3

import textwrap

def wrap(string, max_width):
	lengthofString = len(string)
	remaining_string_length = lengthofString % max_width
	listofstring = []

	for i in range(lengthofString):
		if i % max_width == 0:
			listofstring.append(string[i-max_width:i])
		
	listofstring.append(string[lengthofString-remaining_string_length:])


	parastring = '\n'.join(listofstring[1:])
	return parastring

    

if __name__ == '__main__':
	string, max_width = input(), int(input())
	result = wrap(string, max_width)
	print(result)
