#!/usr/bin/python

import scipy as sp
import numpy as np

from B_FEM import *

#fid = open('input.txt','r')
#print "Printing the file identifier"
#print "-" * 50
#print fid 

print "\n"


#print "Printing file contents"
#print "-" * 50
#text = fid.read()
text = readInput()
#print text
#fid.close()
#properties = readProperties(text)
#constraints = readConstraints(text)
#loads = readLoads(text)
mesh = readMesh(text)

#lines = text.splitlines()

test_element = Element((1.0,0.0),(2.0,0.0),(1,2),1*10**6)

print "\nPrinting a test element's attributes"
print "-" * 50
print test_element



print "\nPrinting element stiffness matrix"
print "-" * 50
print test_element.K[0]
print test_element.K[1]
print test_element.K[2]
print test_element.K[3]

print '-' * 50

#print "Output of the read*() functions:\n"
#print properties
#print constraints
#print loads
print mesh[1]['conn']

test_beam = Beam(text)

#print test_beam.element0
#print "\nElement 0: " + str(test_beam.mesh[0]['conn']) 
#print "\nElement 1: " + str(test_beam.mesh[1]['stop'])

test_beam.assembleGlobalStiffnessMatrix()
