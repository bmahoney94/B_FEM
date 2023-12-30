# B_FEM
Beam finite element solver I created for a class project.

This was my very first 'project' in python.  The intent was to gain some experience with
the language while completing my coursework.  It's not terribly elegant by any means, and
I don't know that I'll ever rework it.

Looking back, it's sort of entertaining to see how hard I worked for something so trivial.
The reading of the file for example is embarrasingly simple when you just use json or similar.
I didn't need to invent my own format and hack my way through some regex...


Basic Feature Set:

	This project uses the finite element method to solve the bending equation on a simple beam.
	The beam is broken into three elements (imposed by the problem definition given in class).
	There is a point load on the end if memory serves.


Suggested Next Steps:

	First and foremost, use the json file instead of a custom test file.
	Add the ability to discretize automatically--don't specify the elements exactly in the file.
	Add some interesting properties to the 'data' field like a changing cross-section.
	Make some plots.
	Connect multiple beam or bar elements into 'frame' and 'struss' elements.

	Also, ditch the object oriented design in favor of data orientation.
