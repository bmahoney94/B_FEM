"""
B_FEM.py is the primary module for my Finite Element project. 

"""
import numpy as np
import scipy as sp
from math import *
	
	
class Element(object):
	"""
	A small 1-D piece of a structural element which has 6 DOF within
	the plane.
	"""
	def __init__(self,start,stop):
		self.length = sqrt((stop[1] - start[1])**2 + (stop[0] - start[0])**2)	# Element length

class Beam(object):
	"""
	A generic, 1-D structural element which can support both axial
	and shear loads.
	"""
	def __init__(self,num_elements,coordinates):
		for i in range(0,num_elements):
			print "Element %d says hello!" % i
		
class Bar(Beam):
	"""
	A 1-D structural element which can only support axial loads.
	"""
	pass

