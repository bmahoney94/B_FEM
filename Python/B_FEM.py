"""
B_FEM.py is the primary module for my Finite Element project. 

"""
import numpy as np
import scipy as sp
import math
from sys import exit
	
class Element(object):
	"""
	A small 1-D piece of a structural element which has 6 DOF within
	the plane.
	"""
	# bend_stiff is E*I, the bending stiffness
	
	def __init__(self,start,stop,connectivity,bend_stiff):
		self.length = math.sqrt((stop[1] - start[1])**2 + (stop[0] - start[0])**2)	# Element length
		self.connectivity = connectivity
		self.bend_stiff = bend_stiff
		# (u1,v1,theta1,u2,v2,theta2)
		self.disp = (0.0,0.0,0.0,0.0,0.0,0.0)
	def __str__(self):
		return """
length = %.4f
connectivity = %s
bending stiffness = %.4f
displacements = %s
""" % (self.length, str(self.connectivity),self.bend_stiff,str(self.disp))
	


	
class Beam(object):
	"""
	A 1-D structural element which can support
	shear loads.
	"""
	def __init__(self,num_elements,coordinates):
		print "number of elements: %s" % num_elements
		elements = []
		for i in range(0,num_elements):
			print "Element %d says hello!" % i
			
		
class Bar(Beam):
	"""
	A 1-D structural element which can only support axial loads.
	"""
	def __init__(self):
		print "This class is not yet implemented!"
		exit()

