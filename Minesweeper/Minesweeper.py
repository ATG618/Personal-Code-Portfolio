import random

class Minesweeper(object):
	""" creates Minesweeper class object for playing Minesweeper game 
	
	Class Behavior: 
		Creates Minesweeper board for game, player selects cells on board until 
		selecting a mine or uncovering all the non-mine cells. When a empty cell
		is selected create the ripple effect(uncovering empty cells in the neighborhood
		of the selected cell)
	
	Public Methods:
		__init__: creates an Minesweeper class object and the listed instance variables.
		populates_values: populates the cell values of the actual board.
		displayBoard: assigns data from board object (player or actual) to a formatted string,
			prints the formatted string. 
		updateCell: updates the actual board cells and player board cells based on row and 
			cell data received as paramaters. 
		__findNeighbors__: determines the neighboring cells relative to a cell given as parameter.
		getInput: prompts user with message, receives input from user, 
			and checks user input for validity.
	Instance Variables:
		actual_board
		player_board 
	"""
	
	
	def __init__(self):
		"""Initialize instance variables for minesweeper object
	
		Instance Variables:
		actual_board: list of list. Board contains cells by row and column. 
			Default Value of row and column = 5
		player_board: list of list. Board contains cells by row and column. 
			Default Value of row and column = 5
		"""
		#Initial Instance Variables 
		self.actual_board = list()
		self.player_board = list()
		
		
		#construct actual board with default dimensions of 5 rows and 5 columns, and starting value 
		#for all cells is None
		self.actual_board = [ 
		[None, None, None, None, None],
		[None, None, None, None, None],
		[None, None, None, None, None],
		[None, None, None, None, None],
		[None, None, None, None, None]
		]
		# self.actual_board = [
		# [2, "M", "E", "E", 3],
		# [4,  1,   7,  "E", 9],
		# [2, "M",  6,   5,  9],
		# [4,  7,  "E", "M", 6],
		# [8,  1,  "E", "E", 3]
		# ]
		
		
		#construct player board with same dimensions as actual board, starting value for all
		#cells is: "H". All cells on player board are hidden by default
		self.player_board = [ 
		["H", "H", "H", "H", "H"],
		["H", "H", "H", "H", "H"],
		["H", "H", "H", "H", "H"],
		["H", "H", "H", "H", "H"],
		["H", "H", "H", "H", "H"]
		]
	
	
	def populate_values(self):
		"""populates the cell values of the actual board.
		
		Input: minesweeper object only (self)
		
		Return: No data is returned from method
		
		User Interaction: No direct interaction with user
		
		Modified Data Structures:
			cells of the actual board class attribute are populated with 3 mines at random, 
			a random number of cells less than or equal to 22 cells are populated with empty value
			"E" and the remaining cells not populated with a value of "M" or "E" are populated with
			a random integer between 1 and 9.
		"""
		
		def placeMines():
			"""place mines at random on actual board.
			
			Input: Same input as populate values. Inner function of populate values
			Return: No data is returned from inner function
			User Interaction: No direct interaction with user
			Modified Data Structure: cells of the actual board class attribute are populated with 3 mines
				at random. 
			"""
			#iterate through for loop 3 times, placing a mine "M" at random locations on actual board cells
			for count in range(0,3):
				row = random.randrange(0,4) 
				column = random.randrange(0,4)
				self.actual_board[row][column] = 'M'
		
		def getCounts():
			"""get Counts of actual board cells to be populated 
			
			Input: Same input as populate values. Inner function of populate values
			Return: No data is returned from inner function
			User Interaction: No direct interaction with user
			Modified Data Structure: cells of the actual board class attribute are populated with 
				with string value "E" a random number of times, remaining cells are populated with 
				integer values between 1 and 9.
			"""
			
			total_board_cells = 25 - 3 #total board cells minus the mines already place
			random_range_of_remain_cells = random.randrange(total_board_cells)
			#iterate through a for loop a random number of times bewteen 0 and 22 times. 
			#assign to a random place in actual board. 
			for count in range(0,random_range_of_remain_cells):	#complete 0-22 times
				row = random.randrange(0,4)
				column = random.randrange(0,4)
				cell = self.actual_board[row][column]
				#if cell is not a mine or has no value assigned. Assign a empty value
				#to cell on actual board
				if cell == None:
					self.actual_board[row][column] = "E"
			
			#for each cell in actual board.if cell is not a mine or empty value 
			#or has no value assigned. Assign a random digit to cell on actual board.
			for row in range(0,5):
				for column in range(0,5):
					row = row - 1
					column = column - 1
					cell = self.actual_board[row][column]
					if cell == None:
						digit_value = random.randrange(1,9) #random digit between 1 and 9
						self.actual_board[row][column] = digit_value
		
		Mined_Cells = placeMines()
		Count_Cells = getCounts()
	
	
	def displayPlayer_Board(self, board):
		""" assigns data from board object (player or actual) to a formatted string
		
		Input: minesweeper object (self). a board class attribute(default parameter) either player board 
			or actual board is received as parameter.
		Return: No data is returned from class method
		User Interaction: Outputs a formatted string of the board object received as parameter
		Modified Data Structure: No modifications made to data received data structures
		"""
		player_board = board
		
		#format string to have row number and column inline with displayed board to user. Data should be
		#aligned.
		player_board_str = '''
		-------Minesweeper----------
		    1   2    3    4    5
		1|  {}   {}    {}    {}    {}
		2|  {}   {}    {}    {}    {}
		3|  {}   {}    {}    {}    {}
		4|  {}   {}    {}    {}    {}
		5|  {}   {}    {}    {}    {}
		
		----------------------------
		'''.format(
		player_board[0][0], player_board[0][1], player_board[0][2], player_board[0][3], player_board[0][4],
		player_board[1][0], player_board[1][1], player_board[1][2], player_board[1][3], player_board[1][4],
		player_board[2][0], player_board[2][1], player_board[2][2], player_board[2][3], player_board[2][4],
		player_board[3][0], player_board[3][1], player_board[3][2], player_board[3][3], player_board[3][4],
		player_board[4][0], player_board[4][1], player_board[4][2], player_board[4][3], player_board[4][4],
		)
		
		print (player_board_str)
		
		
	def updateCell(self, row, column):
		"""updates the actual board cells and player board cells 
		
		Input: minesweeper object (self). row of player board, 
			column of player board. 
		Return: game_state_str is returned to main program
		User Interaction: No direct interaction with user
		Modified Data Structure: cells of the actual board class atttribute and 
			cells of the player board class attribute are modified based on user input received
			as paramters and populated values within cells on each board. 
		
		"""
		def gameLoss():
			"""prints loss message and displays actual board class attributes

			Input: no parameters received. Inner function to update cell
			Return: returns string to updateCell method
			User Interaction: Prints message and actual board class attribute to user
			Modified Data Structure: No data is modified
			"""
			print ("BOOM! You selected a mine. You Lose! You can always try checkers...")
			
			#Display Actual Board
			self.displayPlayer_Board(self.actual_board)
			
			game_state_str = "loss"
			
			return game_state_str
		
		def gameWin():
			"""prints win message and displays actual board class attributes
			
			Input: no parameters received. Inner function to update cell
			Return: returns string to updateCell method
			User Interaction: Prints message and actual board class attribute to user
			Modified Data Structure: No data is modified
			"""
			
			print ("Whoa! You have uncovered all the cells without mines. You Win! You excel at this game.")
			
			#Display Actual Board
			self.displayPlayer_Board(self.actual_board)
			
			game_state_str = "win"
			
			return game_state_str
		
		#assign value in cell to variable for player board and actual board
		actual_board_cell = self.actual_board[row][column] 
		player_board_cell = self.player_board[row][column]
		
		
		if player_board_cell == "H":
			#if mine is uncovered game is over
			if actual_board_cell == "M":
				game_state_str = gameLoss()
				return game_state_str 
			
			elif actual_board_cell in range(1,10):
				player_board_cell = actual_board_cell
				self.player_board[row][column] = player_board_cell
				
				game_state_str = "playing"
				return game_state_str
			#if empty cell is uncovered create the ripple effect
			elif actual_board_cell == "E":
				#uncover the selected cell:
				self.player_board[row][column] = actual_board_cell
				
				#Ripple Effect: uncover other empty cells in relative neighborhood 

				
				#returns a list of values and cell locations within neighboring cells 
				neighboring_cells_list = list()
				neighboring_cells_list = self.__findNeighbors__(row, column)
				# print(neighboring_cells_list)	#Test Code
				
				#iterate through for loop, for each cell value in neighboring cells list assign value to
				#variable.
				for cell_and_location in neighboring_cells_list:
					#iterate through for loop, for each sub list in neighboring cell location list
					related_cell = cell_and_location[0]
					newrow = cell_and_location[1]
					newcolumn = cell_and_location[2]
					
					#if related cell is Not a Cell do nothing, else if related cell is a Mine
					#do nothing, else if related cell is a empty, uncover cell, else if 
					#related cell is a digit value, uncover cell.
					if related_cell == "Not a Cell":
						pass
					elif related_cell == "M":
						pass
					elif related_cell == "E":
						player_board_cell = related_cell
						self.player_board[newrow][newcolumn] = related_cell
					elif related_cell in range(10):
						player_board_cell = related_cell
						self.player_board[newrow][newcolumn] = player_board_cell
				#game continues after finding a empty cell
				game_state_str = "playing"
				return game_state_str
		#iterate through for loops, game is over if there are no remaining "H" 
		#or hidden cells on player board. set variable to true if cells are still hidden. if one
		#cell is not hidden 
		for row in self.player_board:
			for cell in row:
				if cell == "H":
					game_continues = True	#game continues
				else:
					game_continues = False	#no hidden cell at this location
		if game_continues == False:
			game_state_str = gameWin()
			return game_state_str 
		
		
	def __findNeighbors__(self, row, column):
		""" 
		Input: receives minesweeper object (self), row of actual board cell, 
			column of actual board, and string as parameters.
		Return: returns a list of neighboring cell values if string is equal to data. 
			returns a list of lists of neighboring cell locations (row,column) if string is equal to location
		User Interaction: No direct interaction with user
		Modified Data Structure: No data structures are modified.
		"""
		neighboring_cells_list = list()
		 
		
		# PC (1,3) /(0,2)
		# AB 
		# L (1,2)/(0,1) 
		# R (1,4)/(0,3) 
		# B (2,3)/(1,2) 
		# DBL (2,2)/(1,1)  
		# DBR (2,4)/(1,3) 
		# DUL             
		# DUR             
		def assign_cell(row, column):
			"""attempt to assign cell value to variable if cell does not exist assign None"""
			
			
			newrow = row 
			newcolumn = column
			
			#assert that newrow/newcolumn will be above zero, if it is not, overwrite with zero value
			try:
				assert newrow > 0
			except AssertionError:
				newrow = 0
			try:
				assert newcolumn > 0
			except AssertionError:
				newcolumn = 0
			
			#attempt to assign board value to cell, if cell does not exist assign null values
			try:
				cell = self.actual_board[newrow][newcolumn]
				neighboring_cells_list.append([cell,newrow, newcolumn])
			except: #add specific errors later
				#If cell does not exist, use none as placeholder. 
				neighboring_cells_list.append(["Not a Cell", None, None])
			
			#clear data in newrow and newcolumn
			newrow = None
			newcolumn = None
			
			return neighboring_cells_list, newrow, newcolumn
		
		
		#Cell above primary cell
		newrow = row - 1
		newcolumn = column  
		neighboring_cells_list, newrow, newcolumn = assign_cell(newrow, newcolumn)
		
		#Cell below primary cell
		newrow = row + 1
		newcolumn = column
		neighboring_cells_list, newrow, newcolumn = assign_cell(newrow, newcolumn)

		
		#Cell to the right of primary cell
		newrow = row 
		newcolumn = column + 1
		neighboring_cells_list, newrow, newcolumn = assign_cell(newrow, newcolumn)

		#Cell to the left of primary cell
		newrow = row 
		newcolumn = column - 1
		neighboring_cells_list, newrow, newcolumn = assign_cell(newrow, newcolumn)

		#Cell above and to the right of primary cell
		newrow = row - 1
		newcolumn = column + 1
		neighboring_cells_list, newrow, newcolumn = assign_cell(newrow, newcolumn)

		#Cell above and to the left of primary cell
		newrow = row - 1
		newcolumn = column - 1
		neighboring_cells_list, newrow, newcolumn = assign_cell(newrow, newcolumn)

		#Cell below and to the right of primary cell
		newrow = row + 1
		newcolumn = column + 1
		neighboring_cells_list, newrow, newcolumn = assign_cell(newrow, newcolumn)

		#Cell below and to the left of primary cell
		newrow = row + 1
		newcolumn = column - 1
		neighboring_cells_list, newrow, newcolumn = assign_cell(newrow, newcolumn)

		return neighboring_cells_list
	
	
	def getInput(self, userinput_str, userinput_message_str, valid_input_list):
		"""this function prompts and checks user input for validity from list,
		
		asks for user input while input is not in valid input list print error 
		message and ask for new input
		
		Input: minesweeper object (self), user input string, 
			user input message string, list of valid input
		Return: returns a userinput string
		User Interaction: prints message to user, receives input from user, 
		while loop only accepts valid input
		Modified Data Structure: userinput string is modified.
		"""
		
		userinput_str = input(userinput_message_str)
		
		while userinput_str not in valid_input_list: #compare user input against list
			print ("Error. Invalid Input. Please try again")
			userinput_str = input(userinput_message_str)
		
		return userinput_str
	
	
if __name__ == "__main__":
	game = Minesweeper()
	game.populate_values()
	
