#!/usr/bin/python

import scipy as sp
import numpy as np

from B_FEM import *

fid = open('input.txt','r')
print fid
text = fid.read()
print text

lines = text.splitlines()

test_element = Element((1.0,0.0),(2.0,0.0))
print "Element length: %.4f" % test_element.length

test_beam = Beam(2,((0,0),(1,0)))


