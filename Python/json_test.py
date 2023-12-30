

import json

contents = ""
with open( "input.json") as f:
	for line in f:
		contents = contents + str(line)

print( contents)

data = json.loads( contents)
print( data.keys())
