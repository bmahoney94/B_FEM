#!/usr/bin/python

import scipy as sp
import numpy as np

from B_FEM import *

fid = open('input.txt','r')
print "Printing the file identifier"
print "-" * 50
print fid 

print "\n"

print "Printing file contents"
print "-" * 50
text = fid.read()
print text


lines = text.splitlines()

test_element = Element((1.0,0.0),(2.0,0.0),(1,2),5*10**6)

print "\nPrinting a test element's attributes"
print "-" * 50
print test_element
test_beam = Beam(2,((0,0),(1,0)))


print "\nPrinting element stiffness matrix"
print "-" * 50
print test_element.K[0]
print test_element.K[1]
print test_element.K[2]
print test_element.K[3]


