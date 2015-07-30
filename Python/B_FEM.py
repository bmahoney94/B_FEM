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
		self.length = math.sqrt((stop[1] - start[1])**2 + (stop[0] - start[0])**2)	# 2D distance formula 
		self.connectivity = connectivity
		self.bend_stiff = bend_stiff
		self.build_element_stiffness_matrix()
		# (v1,theta1,v2,theta2)
		#self.disp = (0.0,0.0,0.0,0.0)
	def __str__(self):
		output = """
Element Length = %.4f
Connectivity = %s
Bending Stiffness = %.4f
""" % (self.length, str(self.connectivity),self.bend_stiff)
		output += "Element Order: %s" % self.order
		return output
	order = "Linear"	
	
	def build_element_stiffness_matrix(self):
		"""
		Builds element stiffness matrix.
		"""
		K = [[12, 6, -12, 6],[6,4,-6,2],[-12,-6,12,-6],[6,2,-6,4]]
		# make everything into a floating point number
		K = [map(float,K[i]) for i in range(0,len(K))]
		K = np.array(K) 
		K = K * self.bend_stiff
		# This part is a little "un-pythonic"
		K[0,:] = K[0,:] / (self.length**3)
		K[2,:] = K[2,:] / (self.length**3)
		K[1,:] = K[1,:] / (self.length**2)
		K[3,:] = K[3,:] / (self.length**2)

		K[:,1] = K[:,1] * self.length
		K[:,3] = K[:,3] * self.length

		
		self.K = K
		
	
	def nodal_loads(self):
		"""
		Builds vector with equivalent nodal loads.
		"""
		# Unnecessary right now since I have no distributed load
		pass
	
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
########################################################################
def readInput(filename="input.txt"):
	fid = open(filename,'r')
	#print "Printing File Identifier"
	#print fid
	#print "-" * 50
	#print "File contents"
	text = fid.read()
	#print text
	fid.close()
	return text




## Required functions
def readMesh(input_text):
	pass

def readProperties(input_text):
	lines = input_text.splitlines()
	print "Assuming this beam has a square cross-section"
	for line in lines:
		if line.startswith('Problem'):
			print line

def readConstraints(input_text):
	pass

def readLoads(input_text):
	pass

def assembleGlobalStiffnessMatrix(Beam):
	# This is merely a wrapper for the same method in "Beam" being used for project compliance 
	pass

def imposeContraints(Beam):
	pass

def solver(Beam):  # Why do I need this?! I'm just calling a scipy function.
	pass 

def reportResults():
	pass

