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
	returnTuple = tuple(map(tuple, data))
	return returnTuple

def ComputeNeighbors(state):
	hole_coords = [0,0]
	state = list(map(list, state))
	replace = []
	length = len(state)
	for row in range(length):
		for col in range(length):
			if state[row][col] == 0:
				hole_coords[0] = row
				hole_coords[1] = col

	#above 
	if isValid(hole_coords[0] - 1, hole_coords[1], length) == True:
		temp = [row[:] for row in state]
		neighbor = temp[hole_coords[0] - 1][hole_coords[1]]
		temp[hole_coords[0]][hole_coords[1]] = neighbor
		temp[hole_coords[0] - 1][hole_coords[1]] = 0
		tempAdd = tuple(map(tuple, temp))
		tupleAdd = (neighbor, tempAdd)
		replace.append(tupleAdd)

	#below
	if isValid(hole_coords[0] + 1, hole_coords[1], length) == True:
		temp = [row[:] for row in state]
		neighbor = temp[hole_coords[0] + 1][hole_coords[1]]
		temp[hole_coords[0]][hole_coords[1]] = neighbor
		temp[hole_coords[0] + 1][hole_coords[1]] = 0
		tempAdd = tuple(map(tuple, temp))
		tupleAdd = (neighbor, tempAdd)
		replace.append(tupleAdd)

	#right
	if isValid(hole_coords[0], hole_coords[1] + 1, length) == True:
		temp = [row[:] for row in state]
		neighbor = temp[hole_coords[0]][hole_coords[1] + 1]
		temp[hole_coords[0]][hole_coords[1]] = neighbor
		temp[hole_coords[0]][hole_coords[1] + 1] = 0
		tempAdd = tuple(map(tuple, temp))
		tupleAdd = (neighbor, tempAdd)
		replace.append(tupleAdd)

	#left
	if isValid(hole_coords[0], hole_coords[1] - 1, length) == True:
		temp = [row[:] for row in state]
		neighbor = temp[hole_coords[0]][hole_coords[1] - 1]
		temp[hole_coords[0]][hole_coords[1]] = neighbor
		temp[hole_coords[0]][hole_coords[1] - 1] = 0
		tempAdd = tuple(map(tuple, temp))
		tupleAdd = (neighbor, tempAdd)
		replace.append(tupleAdd)
	returnTuple = tuple(replace)
	return returnTuple

def isValid(y,x, length):
	if x >= 0 and x <= length -1:
		if y >= 0 and y <= length -1:
			return True
	return False

def DeBugPrint(state):
	n = len(state)
	row = 0
	print("_____________________________")
	while row < n:
		s = str(state[row]).strip('[]')
		temp = s.replace(",", "	")
		print(temp)
		row = row + 1
	print("_____________________________")

def IsGoal(state):
	length = len(state)
	flattenState = [j for sub in state for j in sub]#Makes the state a single list
	NoHole = flattenState[:(length*length) - 1]
	lastLine = state[length - 1]
	if sorted(NoHole) == NoHole:
		if lastLine[length - 1] == 0:
			return True
	return False

def FindPath(parents, final_state):
	path = []
	tiles = []
	current = parents[final_state]
	tiles.append(parents[final_state])
	count = 1

#create a list of all the states in the path
	while current != None:
		path.append(current)
		current = parents[current]

#find the tiles moved for each state
	for currstate in path:
		if(count < len(path)):
			tiles.append(FindTileChange(path[count], currstate))
			count = count + 1
	tiles.reverse()
	return tiles

def FindTileChange(parent, child):
	for neighbor in ComputeNeighbors(child):
		if neighbor[1] == parent:
			return neighbor[0]

def BFS(state):
	frontier = [state]
	discovered = set(state)
	parents = {state: None}
	while frontier:
		current_state = frontier.pop(0)
		discovered.add(current_state)

		if IsGoal(current_state):
			return FindPath(parents, current_state)

		for neighbor in ComputeNeighbors(current_state):
			if neighbor[1] not in discovered:
				frontier.append(neighbor[1])
				discovered.add(neighbor[1])	
				parents[neighbor[1]] = current_state

def DFS(state):
	frontier = [state]
	discovered = set(state)
	parents = {state: None}

	while frontier:
		current_state = frontier.pop(0)
		discovered.add(current_state)

		if IsGoal(current_state):
			return FindPath(parents, current_state)

		for neighbor in ComputeNeighbors(current_state):
			if neighbor[1] not in discovered:
				frontier.insert(0, neighbor[1]) #add to front
				discovered.add(neighbor[1])	
				parents[neighbor[1]] = current_state



	
state = LoadFromFile(input)
print(BFS(state))
print(DFS(state))

