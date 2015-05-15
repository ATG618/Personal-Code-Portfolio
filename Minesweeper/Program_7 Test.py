from Minesweeper import Minesweeper

def test_init(gameinstance):
	"""test the Minesweeper.__init__ method 
	
	test case 1:check that actual board attribute is a list of lists with None values only
	test case 2:check that player board attribute is a list of lists with "H" string values only
	"""
	try:
		for row in range(0,5):
			for column in range(0,5):
				assert game.actual_board[row][column] == None
	except AssertionError:
		print ("test case 1:check that actual board attribute is a list of lists with None values only")
	else:
		print("test case 1 passed")
	try:
		for row in range(0,5):
			for column in range(0,5):
				assert game.player_board[row][column] == "H"
	except AssertionError:
		print ("test case 2:check that player board attribute is a list of lists with H string values only")
	else:
		print("test case 2 passed")

def test_populate_values(instance):
	"""test the Minesweeper.populate_values method
	
	test case 3: actual board must be a list of list with No None values
	test case 4: player board must be a list of list with "H" string values
	"""
	try:
		for row in range(0,5):
			for column in range(0,5):
				assert game.actual_board[row][column] != None
	except AssertionError:
		print("test case 3: actual board must be a list of list with No None values")
	else:
		print("test case 3 passed")
	
	try:
		for row in range(0,5):
			for column in range(0,5):
				assert game.player_board[row][column] == "H"
	except AssertionError:
		print ("test case 4: player board must be a list of list with H string values")
	else:
		print ("test case 4 passed")

def test_displayPlayer_Board(instance):
	""" test case 5: visually inspect the player board and the actual board."""
	game.displayPlayer_Board(game.actual_board)
	game.displayPlayer_Board(game.player_board)

def test__findNeighbors__(instance):
	"""	test validity of find neighbors function
		
		test case 6: returned output when data string, must be a list of lists with 8 values of either digit 0 to 9, M, or E.
		test case 7: returned output when location string, must be a list of lists with digit 0 to 4, or Not a Cell/None Values
		"""
	
	#assign to variable
	cell_data_list = game.__findNeighbors__(0,0,"data")
	
	try:
		#check that returned object is a list
		assert cell_data_list.append(["test",0])
		cell_data_list.remove(["test",0])	#remove test data
		#check that values in list is either a digit between 0 and 9, M, or E. Must not equal None
		for value in cell_data_list:
			for number in range(0,9):
				if value == number:
					assert value == number
				elif value == "M":
					assert value == "M"
				elif value == "E":
					assert value == "E"
				else:
					assert value != None
	except AssertionError:
		print("test case 6: Error")
	else:
		print("test case 6: Passed")
	
	#assign to variable
	cell_data_list = game.__findNeighbors__(0,0, "location")
	
	try:
		#check that returned object is a list
		assert cell_data_list.append(["Test", 0])
		cell_data_list.remove(["test",0])
		#check that values in list is either a digit between 0 and 4, or Not a Cell and None
		for row in cell_data_list:
			for column in cell_data_list:
				for number in range(0,4):
					assert row == number 
	except AssertionError:
		print("test case 7: Error")
	else: 
		print("test case 7: Pass")

def test_updateCell(instance):
	"""test the functionality of the updateCell class function
	
		test case 8: returned output must be string values only.
		test case 9: gameloss: game loss must return string value only. (Visual Test)
		test case 10: gamewin: game win must return string value only. (Visual Test)
	"""
	#run the updateCell function
	game_str = game.updateCell(1,1)
	try:
		assert game_str + " "
	except AssertionError:
		print("test case 8: Error")
	else:
		print("test case 8: Pass")




if __name__ == "__main__":
	game = Minesweeper()		#initialize minesweeper class instance
	test_init(game)				#test initialized game 
	game.populate_values()		#run populate values of minesweeper 
	test_populate_values(game)	#test populate values in list of lists 
	test_displayPlayer_Board(game)	#test display of actual and player board
	test__findNeighbors__(game)
	test_updateCell(game)
	
