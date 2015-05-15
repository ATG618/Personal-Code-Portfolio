#CS 101
#Program 7
#Alfred Harris
#ajhyr9@mail.umkc.edu
#Problem: 
# 	Create Minesweeper game using preformatted class and class functions, and
#	any additional class functions and code as needed.
#Algorithm: 
# Program 7 Algorithm:
	# 1-Construct objects neccessary for Minesweeper Game to run
		# Objects Required: Actual Board, Player Board, Board Dimensions-Player, 
		# Board Dimensions- Actual, Cell Hidden Property for player Board, 
		# Cells to be Hidden on Player Board, Game State
	# 2-Populate values of actual board:
		# Randomly place mines(3) in cells on actual board 
		# Populate remaining cells on actual board with empty cell or actual digit between 1 and 9
	# 3-Display cells on player board:
		# Default view for cells on player board: 'H'
		# Update view as player changes cells on actual board
		# Include Row Number and Column Number on player board
	# 4-Prompt player to choose a board position to explore:
		# If selected cell already has hidden property set to false --> Reprompt for board position
		# If selected cell hidden property is set to true --> 
			# If selected cell contains a Mine --> 
				# Print Message: 'BOOM, Mine was hit,Game Over!'
				# Display Actual Board
				# Set game state to lose 
			# If selected cell contains a Digit --> 
				# Change cell hidden property on actual board to False 
				# Display related actual board cell value on player board
			# If selected call contains a Empty Value --> 
				# create Ripple Effect: 
					# move horizontally, vertically, and diagonally
					# Iterate through list of neighboring cells:
						# If related cell is Empty --> 
							# run uncover_Cell function
							# continue iteration of list
							# add to ripple effect queue list 
						# Else If related cell is a Mine or Digit -->
							# run uncover_Cell function
							# break iteration
						# Else If related cell is End of Board -->
							# break iteration
					# Iterate through list of ripple effect queue list:
						# same process as Iterate through list of neighboring cells
	# 5-If player uncovers all non-mine cells  --> 
		# set game state to win, print winner message
		# prompt player to play again
			# if yes --> set game state to 'playing'
			# if no --> end program 



from Minesweeper import Minesweeper
#Initial value is set to playing
game_state_str = "playing"

while game_state_str == "playing":
	#Create Minesweeper object and assign to variable game
	game = Minesweeper()
	#Populate all objects required to play game
	game.populate_values()
	#Display player board to player
	game.displayPlayer_Board(game.player_board)
	#Prompt player to enter cell to uncover on minesweeper board. 
	userinput_message_str = "Select the Cell you want to uncover."
	userinput_message_str2 = "Enter Row Number of Cell: " 
	userinput_message_str3 = "Enter Column Number of Cell: "
	userinput_str = ""
	valid_input_list = ["1","2","3","4","5"]
	
	print(userinput_message_str)
	
	validinput_bool = True
	while validinput_bool == True:
		#Prompt player to input row number and column number to uncover. If row number is 
		#not within valid input list, continue to ask for valid input. convert input to integer
		#data type and assign to row and column respectively
		row = int(game.getInput(userinput_str, userinput_message_str2, valid_input_list)) - 1
		column = int(game.getInput(userinput_str, userinput_message_str3, valid_input_list)) - 1
		#run update cell class function taking row and column data as parameters. 
		game_state_str = game.updateCell(row,column)
		
		#if returned value is string equal to loss, set game state to loss, and break out of 
		#valid input while loop.
		if game_state_str == "loss":
			validinput_bool = False
		#else if returned value is string equal to win, set game state to win, and break out of
		#valid input while loop.
		elif game_state_str == "win":
			validinput_bool = False
		elif game_state_str == "playing":
			validinput_bool = True
			game.displayPlayer_Board(game.player_board)
		
	if game_state_str == "loss" or game_state_str == "win":
		#Prompt player to play again. If player input is not within valid input print error message
		#and continue to prompt for player input.
		userinput_message_str = "Would you like to play again. Y or N: "
		userinput_str = ""
		valid_input_list = ["yes","no","y","n"]
		
		userinput_str = input(userinput_message_str)
		userinput_str = userinput_str.lower()
		while userinput_str not in valid_input_list:
			print("Error. Please use correct input")
			userinput_str = input(userinput_message_str)
		
		#if player wants to play again set game state to playing
		if userinput_str == "y":
			game_state_str = "playing"
		#else if player wants to quit set game state to quit
		elif userinput_str == "n":
			game_state_str = "quit"
