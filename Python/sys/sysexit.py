#!/usr/bin/python3
import sys
a=input()
#print('Hello world!')
if int(a) <= 5:
    print("Entered value is less than or equal to 5")
    sys.exit(5)
else:
    print("Entered value is greater than 5")
    sys.exit(10)

# Custom exit code can be generated based on the conditional statement being exected. The exit code can be caputed in the terminal / shell using $?