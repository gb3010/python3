#!/usr/bin/python3
import sys

print("Name of the script is ", sys.argv[0])
# print("The first argument is ",sys.argv[1])
print("All the arguments are ",sys.argv)
k=len(sys.argv)
print("Number of arguments is ",k-1)

print("All arguments together ",*sys.argv,sep=' ') #This is a pointer representation of array which can be used with sep variable of print

'''
sys.argv accepts positional parameters
sys.argv is a list representation of the command line arguments, with the name of the script as first element
Number of arguments can be obtained from length of the list - 1
'''