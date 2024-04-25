import copy

# Heuristic function to calculate the Manhattan distance
def hn(state, finalstate):
	count = 0
	for i in range(3):
		for j in range(3):
			if(state[i][j]!=-1):
				if(state[i][j] != finalstate[i][j]):
					count+=1
	return count

# Function to find the position of the blank tile (-1)
def findposofblank(state):
	for i in range(3):
		for j in range(3):
			if(state[i][j] == -1):
				return [i,j]

# Move functions for each direction
def move_left(state, pos):
	if(pos[1]==0):  # if already in leftmost column, cannot move left
		return None
	retarr = copy.deepcopy(state)
	retarr[pos[0]][pos[1]],retarr[pos[0]][pos[1]-1] = retarr[pos[0]][pos[1]-1],retarr[pos[0]][pos[1]]
	return retarr

def move_up(state, pos):
	if(pos[0]==0):  # if already in top row, cannot move up
		return None
	retarr = copy.deepcopy(state)
	retarr[pos[0]][pos[1]],retarr[pos[0]-1][pos[1]] = retarr[pos[0]-1][pos[1]],retarr[pos[0]][pos[1]]
	return retarr

def move_right(state, pos):
	if(pos[1]==2):  # if already in rightmost column, cannot move right
		return None
	retarr = copy.deepcopy(state)
	retarr[pos[0]][pos[1]],retarr[pos[0]][pos[1]+1] = retarr[pos[0]][pos[1]+1],retarr[pos[0]][pos[1]]
	return retarr

def move_down(state, pos):
	if(pos[0]==2):  # if already in bottom row, cannot move down
		return None
	retarr = copy.deepcopy(state)
	retarr[pos[0]][pos[1]],retarr[pos[0]+1][pos[1]] = retarr[pos[0]+1][pos[1]],retarr[pos[0]][pos[1]]
	return retarr

# Function to print the matrices array
def printMatrix(matricesArray):
	print("")
	counter = 1
	for matrix in matricesArray:
		print("Step {}".format(counter))
		for row in matrix:
			print(row)
		counter+=1
		print("")

# Main function for eight puzzle solving
def eightPuzzle(initialstate, finalstate):
	gn=0
	explored = []
	while(True):
		explored.append(initialstate)
		if(initialstate == finalstate):
			break
		gn+=1
		# Generate possible moves
		left = move_left(initialstate, findposofblank(initialstate))
		right = move_right(initialstate, findposofblank(initialstate))
		up = move_up(initialstate, findposofblank(initialstate))
		down = move_down(initialstate, findposofblank(initialstate))
		# Calculate heuristic values for each move
		fnl=1000
		fnr=1000
		fnu=1000
		fnd=1000
		if(left!=None):
			fnl = gn + hn(left,finalstate)
		if(right!=None):
			fnr = gn + hn(right,finalstate)
		if(up!=None):
			fnu = gn + hn(up,finalstate)
		if(down!=None):
			fnd = gn + hn(down,finalstate)
		# Choose the move with minimum heuristic value
		minfn = min(fnl, fnr, fnu, fnd)
		if((fnl == minfn) and (left not in explored)):
			initialstate = left
		elif((fnr == minfn) and (right not in explored)):
			initialstate = right
		elif((fnu == minfn) and (up not in explored)):
			initialstate = up
		elif((fnd == minfn) and (down not in explored)):
			initialstate = down
	# Print the steps taken to reach the final state
	printMatrix(explored)

# Main function to take input and start the program
def main():
	while(True):
		start = []
		print("START STATE")
		for i in range(3):
			arr=[]
			for j in range(3):
				a = int(input("Enter element at  {},{}: ".format(i,j)))
				arr.append(a)
			start.append(arr)
		final = []
		print("\nFINAL STATE")
		for i in range(3):
			arr=[]
			for j in range(3):
				a = int(input("Enter element at  {},{}: ".format(i,j)))
				arr.append(a)
			final.append(arr)
		# Call the eightPuzzle function with initial and final states
		eightPuzzle(start, final)

# Execute the main function
main()
