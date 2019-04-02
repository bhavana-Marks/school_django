import json

# Read file 

def loadHyd():
	f = open('schools\static\schoolList\json\\hyderabad.json')
	json_string = f.read()

	f.close()

	print(json_string)