#!/usr/bin/python3
import sys

a='hi'

if a == 'hi':
    sys.stderr.write('Error!')


# The output generated by stderr can be suppressed using 2> while executing in terminal, whereas it gets printed in the stdout by default