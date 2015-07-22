"""
B_FEM.py is the primary module for my Finite Element project. 

"""
import numpy as np
import scipy as sp

def Structure(object):
"""
Contains the global properties of the particular problem formulation.

"""
	pass

def Beam(object):
"""
A generic, 1-D structural element which can support both axial
and shear loads.
"""
	pass

def SimpleBeam(Beam):
"""
A 1-D structural element which can only support shear loads.
"""
	pass

def Bar(Beam):
"""
A 1-D structural element which can only support axial loads.
"""
	pass

def Element(object):
"""
A small 1-D peice of a structural element which has 6 DOF within
the plane.
"""
	pass

def Truss(Structure):
	pass

def Frame(Structure):
	pass





