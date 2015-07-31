"""
B_FEM.py is the primary module for my Finite Element project. 

"""
import numpy as np
import scipy as sp
import math
from sys import exit
import re
	
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
	def __init__(self,num_elements):
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
	"""
	Reads the input file and returns a string with all of the text.
	"""
	fid = open(filename,'r')
	text = fid.read()	
	fid.close()
	return text




## Required functions
def readMesh(input_text):
	"""
	Reads information about the number of elements and nodal
	connectvities.
	"""
	print "\nReading mesh properties"
	element = {}
	mesh = []	
	lines = input_text.splitlines()
	i = 0
	for line in lines:
		
		if line.startswith('Elements:'):
			print line
			try:
				start = re.search('start:"(.+?)"',line).group(1)
				stop = re.search('stop:"(.+?)"',line).group(1)
				connectivity = re.search('vity:"(.+?)"',line).group(1)
			except:
				print "Failed to parse Mesh properties."
				exit(1)
			i +=1
			print "Element %d" % i
			print "Start: " + start
			print "Stop: " + stop
			print "Connectivity: " + connectivity
			element = {"ID":i,"start":start,"stop":stop,"Conn":connectivity}
			mesh.append(element)

	return mesh
def readProperties(input_text):
	"""
	Reads beam properties.  Right now, just the bending stiffness.
	"""
	print "\nReading beam properties"
	lines = input_text.splitlines()
	
	for line in lines:
		if line.startswith('Problem'):
			print line
			try:
				found = re.search('Stiffness:(.+?)}',line).group(1)
			except AttributeError:
				print "Failed to parse properties from input.txt"
				exit(1)
			print "Bending stiffness input: " + found
	return float(found) 

def readConstraints(input_text):
	"""
	Reads and parses the kinematic constraints.
	"""
	print "\nReading contraints"

	constraints = []
	lines = input_text.splitlines()
	for line in lines:
		if line.startswith('Constraint'):
			print line
			try:
				found = re.search('{(.+?)}',line).group(1)
			except:
				print "Failed to parse constraints."
				exit(1)
			print found 
			constraints.append(found)

	return constraints


def readLoads(input_text):
	"""
	Reads and parses the specified loads.
	"""
	loads = []
	print "\nReading loads"
	lines = input_text.splitlines()
	for line in lines:
		if line.startswith('Forces'):
			print line
			try:
				# Does not find applied moments currently
				position = re.search("position:(.+?),",line).group(1)
				force = re.search("force:(.+?)}",line).group(1)
			except AttributeError:
				print "Failed to parse applied loads"
				exit(1)
			print "Location: " + position
			print "Force: " + force
			loads.append(position)
			loads.append(force)
		
	return loads	
	

def assembleGlobalStiffnessMatrix(Beam):
	# This is merely a wrapper for the same method in "Beam" being used for project compliance 
	pass

def imposeContraints(Beam):
	pass

def solver(Beam):  # Why do I need this?! I'm just calling a scipy function.
	pass 

def reportResults():
	pass

