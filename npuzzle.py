import math
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

def ComputeNeighbors(state):
	hole_coords = [0,0]
	replace = []
	length = len(state) - 1
	for row in range(length):
		for col in range(length):
			if state[row][col] == 0:
				hole_coords[0] = row
				hole_coords[1] = col
	print(hole_coords)

	#above 
	if isValid(hole_coords[0] - 1, hole_coords[1], length) == True:
		temp = [row[:] for row in state]
		neighborCord = temp[hole_coords[0] - 1][hole_coords[1]]
		temp[hole_coords[0]][hole_coords[1]] = neighborCord
		temp[hole_coords[0] - 1][hole_coords[1]] = 0
		replace.append([neighborCord, temp])

	#below
	if isValid(hole_coords[0] + 1, hole_coords[1], length) == True:
		temp = [row[:] for row in state]
		neighborCord = temp[hole_coords[0] + 1][hole_coords[1]]
		temp[hole_coords[0]][hole_coords[1]] = neighborCord
		temp[hole_coords[0] + 1][hole_coords[1]] = 0
		replace.append([neighborCord, temp])

	#right
	if isValid(hole_coords[0], hole_coords[1] + 1, length) == True:
		temp = [row[:] for row in state]
		neighborCord = temp[hole_coords[0]][hole_coords[1] + 1]
		temp[hole_coords[0]][hole_coords[1]] = neighborCord
		temp[hole_coords[0]][hole_coords[1] + 1] = 0
		replace.append([neighborCord, temp])

	#left
	if isValid(hole_coords[0], hole_coords[1] - 1, length) == True:
		temp = [row[:] for row in state]
		neighborCord = temp[hole_coords[0]][hole_coords[1] - 1]
		temp[hole_coords[0]][hole_coords[1]] = neighborCord
		temp[hole_coords[0]][hole_coords[1] - 1] = 0
		replace.append([neighborCord, temp])
	return replace

def isValid(y,x, length):
	if x >= 0 and x <= length -1:
		if y >= 0 and y <= length -1:
			return True
	return False

def format(state):
	n = len(state)
	row = 0
	print("_____________________________")
	while row < n:
		s = str(state[row]).strip('[]')
		temp = s.replace(",", "	")
		print(temp)
		row = row + 1
	print("_____________________________")

def isGoal(state):
	longlist = []
	length = len(state)
	i = 0
	while i < len(state):
		if (all(i < j for i, j in zip(state, state[i:i+4]))) == False:
			return False
		i = i + 4
	return True
	
def BFS(state):
	frontier = [state]
	discovered = state
	string_ints = [str(int) for int in state]
	og_key = ",".join(string_ints)
	parents = {og_key: None}

	while len(frontier) != 0:
		current_state = frontier.pop(0)
		discovered.add(tuple(current_state))
	
		print(isGoal(current_state))
		if isGoal(current_state):
			return sorted(parents.items())
	
		neighbor = ComputeNeighbors(current_state)
		for current in neighbor:
			print("gotHere 1")
			print(current[1])
			print(discovered)
			if current[1] in discovered:
				print("gotHere 2")
				frontier.append(neighbor)
				discovered.append(neighbor)
				print("current")
				print(current[0])
				parents[current[0]] = current_state
				print(parents)


state = LoadFromFile(input)

#for grid in temp:
#	format(grid[1])
print(BFS(state))

