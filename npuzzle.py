from array import *
input = open("input.txt", "r")

def LoadFromFile(filepath):
	valid = False
	n = int(filepath.readline())
	row = 0
	data = []
	error_message = "txt file inputed is invalid. try again"
	
	#creates a list of lists
	while row < n:
		temp = []
		s = filepath.readline()
		temp = s.replace("*", "0").split() #makes the list of strings
		if "0" in temp:
			valid = True
		if len(temp) != n: #checks if row is correct length
			return error_message
		temp = [int(i) for i in temp]
		data.append(temp)
		row = row + 1
	if len(data) != n: #Checks if it has the right number of rows
		return error_message
#checks to see if a hole is in the txt
	if valid == False:
		return error_message
	return data

state = LoadFromFile(input)
print(state)

