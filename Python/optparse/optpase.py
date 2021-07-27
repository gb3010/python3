#!/usr/bin/python3
from optparse import OptionParser
op = OptionParser()
op.add_option("-f","--fruit",dest="fruit",help="The fruit name to be entered.")
op.add_option("-v","--veggie",dest="veggie",help="Vegetable name to be entered")
(optionval, argval) = op.parse_args()

print("Fruits are %s" % optionval.fruit)
print("Veggies are %s" % optionval.veggie)
print("The remaining options are %s" % str(argval))
