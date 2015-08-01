#!/usr/bin/python

import scipy as sp
import numpy as np

from B_FEM import *

text = readInput()
print "\n\nThe input file's text:\n"
print text
mesh = readMesh(text)

test_beam = Beam(text)

assembleGlobalStiffnessMatrix(test_beam)
imposeConstraints(test_beam)
solver(test_beam)

reportResults(test_beam)
