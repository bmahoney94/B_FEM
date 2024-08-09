#!/usr/bin/python

import scipy as sp
import numpy as np

from B_FEM import *

text = readInput()
print("\n\nThe input file's text:\n")
print(text)
mesh = readMesh(text)

test_beam = Beam(text)

assembleGlobalStiffnessMatrix(test_beam)
imposeConstraints(test_beam)
solver(test_beam)

reportResults(test_beam)
criteria = np.array( [0., -1.42857143e-4, 0., 0., 0., 3.57142857e-5, 3.0952381e-3, -3.92857143e-4])
#print( test_beam.nodal_displacements - criteria)
assert( np.linalg.norm( test_beam.nodal_displacements - criteria) < 1e-7)
