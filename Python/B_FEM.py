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
	A small 1-D piece of a structural element.	
	"""
	# bend_stiff is E*I, the bending stiffness
	order = "Linear"	
	def __init__(self,start,stop,connectivity,bend_stiff):
	
		self.length = math.sqrt((stop[1] - start[1])**2 + (stop[0] - start[0])**2)	 
		self.connectivity = connectivity
		self.bend_stiff = bend_stiff
		self.build_element_stiffness_matrix()
		# (v1,theta1,v2,theta2)
		#self.disp = (0.0,0.0,0.0,0.0)

#			print "Beam element failed to initialize."
#			print "Exiting now."
#			exit()
	def __str__(self):
		output = """
Element Length = %.4f
Connectivity = %s
Bending Stiffness = %.4f
""" % (self.length, str(self.connectivity),self.bend_stiff)
		output += "Element Order: %s" % self.order
		return output
	
	
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

	def __init__(self,text):
		
		self.bend_stiff = float(readProperties(text))
		self.mesh = readMesh(text)
		self.constraints = readConstraints(text)
		self.forces = readLoads(text)
		self.num_elements = len(self.mesh)
		self.elements = []
		for i in xrange(0,self.num_elements):
			self.elements.append(Element(self.mesh[i]['start'],self.mesh[i]['stop'],self.mesh[i]['conn'],self.bend_stiff))
			


			
	def __str__(self):
		output = "\nBending stiffness: %.4f" % self.bend_stiff
		output += "\nMesh Parameters: " + str(self.mesh)
		output += "\nNumber of Elements: %d" % len(self.mesh) 
		output += "\nConstraints: " + str(self.constraints)
		output += "\nLoads: " + str(self.forces)
		return output
	

	def assembleGlobalStiffnessMatrix(self):
		"""
		Pretty self explanatory.  Uses member elements of the
		particular beam instance to build the stiffness matrix for
		said beam.
		"""
		self.K_global = np.zeros((8,8))
		# Don't forget indices start at 0!!
		self.K_global[:2,:2]   += self.elements[0].K[2:,2:]
		self.K_global[6:8,6:8] += self.elements[0].K[:2,:2]
		self.K_global[:2,-2:]  += self.elements[0].K[-2:,:2]	
		self.K_global[-2:,:2]  += self.elements[0].K[:2,-2:]
		print self.K_global
	
		# TODO: Now add the other 2 element contributions
		self.K_global[:2,:2]   += self.elements[1].K[:2,:2]		
		self.K_global[:2,4:6]  += self.elements[1].K[:2,2:]	
		self.K_global[4:6,:2]  += self.elements[1].K[2:,:2]
		self.K_global[4:6,4:6] += self.elements[1].K[2:,2:]
		print self.K_global
		
		self.K_global[4:6,4:6] += self.elements[2].K[:2,:2]
		self.K_global[4:6,2:4] += self.elements[2].K[:2,2:]
		self.K_global[2:4,4:6] += self.elements[2].K[2:,:2]
		self.K_global[2:4,2:4] += self.elements[2].K[2:,2:]
		print self.K_global/1000.


		
class Bar(Beam):
	"""
	A 1-D structural element which can only support axial loads.
	"""
	def __init__(self):
		print "This class is not yet implemented!"
		exit(1)



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
	#print "\nReading mesh properties"
	element = {}
	mesh = []	
	lines = input_text.splitlines()
	i = 0
	for line in lines:
		
		if line.startswith('Elements:'):
			#print line
			try:
				start = re.search('start:"(.+?)"',line).group(1).split(',')
				stop = re.search('stop:"(.+?)"',line).group(1).split(',')
				connectivity = re.search('vity:"(.+?)"',line).group(1).split(',')
			except:
				print "Failed to parse Mesh properties."
				exit(1)
			i +=1
			#print "Element %d" % i
			#print "Start: " + str(start)
			#print "Stop: " + str(stop)
			#print "Connectivity: " + str(connectivity)
			start = map(float,start)
			stop = map(float,stop)
			connectivity = map(int,connectivity)
			#print type(start[0])
			element = {"ID":i,"start":start,"stop":stop,"conn":connectivity}
			mesh.append(element)

	return mesh




def readProperties(input_text):
	"""
	Reads beam properties.  Right now, just the bending stiffness.
	"""
	#print "\nReading beam properties"
	lines = input_text.splitlines()
	
	for line in lines:
		if line.startswith('Problem'):
			#print line
			try:
				bend_stiff = re.search('Stiffness:(.+?)}',line).group(1)
			except:
				print "Failed to parse properties from input.txt"
				exit(1)
			#print "Bending stiffness input: " + bend_stiff
	return float(bend_stiff) 






def readConstraints(input_text):
	"""
	Reads and parses the kinematic constraints.
	"""
	#print "\nReading contraints"

	constraints = []
	lines = input_text.splitlines()
	for line in lines:
		if line.startswith('Constraint'):
			#print line
			try:
				found = re.search('{(.+?)}',line).group(1)
			except:
				print "Failed to parse constraints."
				exit(1)
			#print found 
			constraints.append(found)

	return constraints


def readLoads(input_text):
	"""
	Reads and parses the specified loads.
	"""
	loads = []
	#print "\nReading loads"
	lines = input_text.splitlines()
	for line in lines:
		if line.startswith('Forces'):
			#print line
			try:
				# Does not find applied moments currently
				position = re.search("position:(.+?),",line).group(1)
				force = re.search("force:(.+?)}",line).group(1)
			except:
				print "Failed to parse applied loads"
				exit(1)
			#print "Location: " + position
			#print "Force: " + force
			loads.append(position)
			loads.append(force)
		
	return loads	
	

def assembleGlobalStiffnessMatrix(Beam):
	# It makes more sense for this to be a member function of the "beam" class.  This one is not functional.
	pass

def imposeContraints(Beam):
	# Refer to Beam.imposeConstraints above.  This is not functional.
	pass

def solver(Beam):
	# Refer to the "Beam" class.  This function does nothing.  It's just a reminder for me.
	pass 

def reportResults():
	pass

