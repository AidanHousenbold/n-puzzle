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
	length = len(state)
	for row in range(length):
		for col in range(length):
			if state[row][col] == 0:
				print("entered")
				hole_coords[0] = row
				hole_coords[1] = col
	print(hole_coords)

	#above 
	if isValid(hole_coords[0] - 1, hole_coords[1], length) == True:
		temp = [row[:] for row in state]
		neighborCord = temp[hole_coords[0] - 1][hole_coords[1]]
		temp[hole_coords[0]][hole_coords[1]] = neighborCord
		temp[hole_coords[0] - 1][hole_coords[1]] = 0
		print(state)
		print([neighborCord, temp])
		replace.append([neighborCord, temp])

	#below
	if isValid(hole_coords[0] + 1, hole_coords[1], length) == True:
		temp = [row[:] for row in state]
		neighborCord = temp[hole_coords[0] + 1][hole_coords[1]]
		temp[hole_coords[0]][hole_coords[1]] = neighborCord
		temp[hole_coords[0] + 1][hole_coords[1]] = 0
		print(state)
		print([neighborCord, temp])
		replace.append([neighborCord, temp])

	#right
	if isValid(hole_coords[0], hole_coords[1] + 1, length) == True:
		temp = [row[:] for row in state]
		neighborCord = temp[hole_coords[0]][hole_coords[1] + 1]
		temp[hole_coords[0]][hole_coords[1]] = neighborCord
		temp[hole_coords[0]][hole_coords[1] + 1] = 0
		print(state)
		print([neighborCord, temp])
		replace.append([neighborCord, temp])

	#left
	if isValid(hole_coords[0], hole_coords[1] - 1, length) == True:
		temp = [row[:] for row in state]
		neighborCord = temp[hole_coords[0]][hole_coords[1] - 1]
		temp[hole_coords[0]][hole_coords[1]] = neighborCord
		temp[hole_coords[0]][hole_coords[1] - 1] = 0
		print(state)
		print([neighborCord, temp])
		replace.append([neighborCord, temp])

def isValid(y,x, length):
	if x >= 0 and x <= length -1:
		if y >= 0 and y <= length -1:
			print("got here")
			return True
	print("got False")
	return False

def isGoal(state)
	
def BFS(state):
	frontier = [state]
	discovered = {tuple(state)}
	parents = {tuple(state): None}
	while len(frontier) != 0:
		current_state = frontier.pop(0)
		discovered.add(tuple(current_state))

	if IsGoal(current_state):
		you're done
		return the path you need by backtracking in parents
	for neighbor in ComputeNeighbors(current_state):
		if the neighbor isn't already in the discovered set
			add the neighbor to the end of the frontier
			mark the neighbor as discovered
			add neighbor: current_state to the parents map


state = LoadFromFile(input)
ComputeNeighbors(state)

