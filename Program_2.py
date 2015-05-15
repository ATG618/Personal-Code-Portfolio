#CS 101
#Program 1
#Alfred Harris
#ajhyr9@mail.umkc.edu
#Problem:
#In the game of Lucky Sevens, player's will lose over the long term, but player's
#aren't aware of the of the mathematical basis of their odds of winning at Lucky Sevens
#write a program that demonstrates the long term outcome of playing Lucky Sevens
#Algorithm:
#1.	print welcome message to user, and prompt user to choose whether or not to play casino game
#	a.	if user input is yes then set game status equal to true
#2.	while game status is equal to true run remaining steps of program, otherwise print farewell message to console #and exit program.
#3.	prompt user to input amount for player pot, convert input from string data type to integer data type. set #player pot equal to converted user input.
#a.	if input is less than zero then print error message, repeat user input prompt
#4.	prompt user to choose whether or not they want detailed output of game results
#a.	if user input is Yes or yes then set detailed output equal to true else if user input is no or No then set detailed output equal to false
#5.	increment round number value by 1, produce a random value for dice a and dice b between 1 and 6.  set dice a #rolled and dice b rolled equal to random values computed respectively. set total of dice rolled equal to the sum of #the values of dice a rolled and dice b rolled.
#6.	if the total of dice rolled is equal to winning dice roll then set round payout equal to round win otherwise set #round payout equal to round loss.
#7.	add the computed round payout to the player pot, and add value of player pot to the end of the list of player #pot values.
#8.	 if detailed output is set equal to true then print to console: round number, dice a rolled, dice b rolled, #total of dice rolled, round payout, and player pot.
#9.	when player pot becomes equal to zero then set max pot size equal to the largest number in the list of player #pot values, print: round number and max pot size to console.
#10.	prompt user to choose whether or not to play casino game again.
#	a.	if user input is Yes or yes then set all variables except (round win, round loss, and winning dice roll) #equal to zero or null. note: program will continue from step 3.
#b.	if user input is No or no: set game status equal to false.  note: program will terminate.

import random, math, gc

#Initial Variable Values
Game_Status_bool = None
Players_Pot_int = 0
Players_Pot_str = " " 
Detailed_Game_Output_str = " "
Detailed_Game_Output_bool = None
Round_Number_int = 0
Dice_Rolled_A_int = 0
Dice_Rolled_B_int = 0
Round_Payout_int = 0
Total_of_Dice_Rolled_int = 0
Detailed_Input_per_Round_List = [Round_Number_int, Dice_Rolled_A_int, Dice_Rolled_B_int, Total_of_Dice_Rolled_int,Round_Payout_int, Players_Pot_int]
Detailed_Output_per_Round_List = [List_of_Round_Number_int_List, List_of_Dice_Rolled_A_int_List, List_of_Dice_Rolled_B_int_List, List_of_Total_of_Dice_Rolled_int_List, List_of_Round_Payout_int_List, List_of_Player_Pot_Values_int_List]
List_of_Player_Pot_Values_int_List = []
List_of_Dice_Rolled_A_int_List = []
List_of_Dice_Rolled_B_int_List = []
List_of_Total_of_Dice_Rolled_int_List = []
List_of_Round_Payout_int_List = []
List_of_Round_Number_int_List = []
Detailed_Output_str = " "
Max_Player_Pot_Size_of_All_Rounds_int = 0
Final_Game_Results_Output_str = " "
Play_Again_str = " "
#Constant Literal Variable Unchanging
Winning_Dice_Roll_int = 7
Round_Win_Amount_int = 4
Round_Loss_Amount_int = -1
Farewell_Message_str = "Thanks for using Lucky Sevens Game Analysis 1.0!"
Welcome_Message_str = "Welcome to Lucky Sevens Game Analysis 1.0"

#print welcome message to user and ask user to choose whether or not to play
print (Welcome_Message_str)
PlayGame_Choice_str = input("Would you like to run the Lucky Sevens Game Analysis? yes or no:")

#if player inputs yes set game status to True, if player inputs no set game status to False
if PlayGame_Choice_str == "yes":
	Game_Status_bool = True 
elif PlayGame_Choice_str == "no":
	Game_Status_bool = False

#while Game Status is set to True run nested code, otherwise print a farewell message and end the program 
while Game_Status_bool == True:
	Players_Pot_str = input("How much do you want your starting pot to be?:")
	
	#convert string input to integer data type and store in variable
	Players_Pot_int = int (Players_Pot_str) 
	
	# if Player Pot is less than zero print error and prompt user for input again. 
	if Players_Pot_int < 0: 
		print ("Error: User Input is less than zero Renter Input")
		Players_Pot_str = input("Please enter starting amount of players pot")
		Players_Pot_int = int (Players_Pot_str)
	
	# ask user whether or not to give detailed output of game results Note: pot size over 300 have caused complete pc failure when detailed output is on.
	Detailed_Game_Output_str = input ("Would you like to get detailed game results? yes or no:")
	
	# if user input "yes" then set Detailed Game Results to True otherwise set to False
	if Detailed_Game_Output_str == "yes":
		Detailed_Game_Output_bool = True 
	else:
		Detailed_Game_Output_bool = False 
	
	'''while Player Pot is less than 0 increase round by 1, produce random value for dice A and B, sum dice rolls for A and B, if winning dice roll increase player pot otherwise decrease player pot'''
	while Players_Pot_int != 0:
		Round_Number_int += 1
		Dice_Rolled_A_int = random.randint(1,6)
		Dice_Rolled_B_int = random.randint(1,6)
		Total_of_Dice_Rolled_int = Dice_Rolled_A_int + Dice_Rolled_B_int 
		'''If the total of dice rolled is equal to winning dice amount set round payout equal to round win amount otherwise set round payout equal to round loss amount'''
		if Total_of_Dice_Rolled_int == Winning_Dice_Roll_int:
			Round_Payout_int = Round_Win_Amount_int
		else:
			Round_Payout_int = Round_Loss_Amount_int
		Players_Pot_int += Round_Payout_int 
		#For Loop  that Adds new values to the end of the corresponding list for each detailed output variable
		for Output in Detailed_Output_per_Round_List:
			for Input in Detailed_Input_per_Round_List:
			Output.append(Input)

		#if detailed game ouput was selected print all detailed output inside of a formatted string
	if Detailed_Game_Output_bool == True: 
		Detailed_Output_per_Round_List = [List_of_Round_Number_int_List, List_of_Dice_Rolled_A_int_List, List_of_Dice_Rolled_B_int_List, List_of_Total_of_Dice_Rolled_int_List, List_of_Round_Payout_int_List, List_of_Player_Pot_Values_int_List]
		
		Detailed_Output_str = "Round Number: {:,} Dice A Rolled: {} Dice B Rolled: {} Total of Dice A and B: {}  Payout at Round {}: {} Player Pot: {:,}".format(Round_Number_int, Dice_Rolled_A_int, Dice_Rolled_B_int,Total_of_Dice_Rolled_int,Round_Number_int, Round_Payout_int, Players_Pot_int)
		print (Detailed_Output_str)
		
	# if player pot is equal to zero find max pot value in list of player pot values and print values to console
	if Players_Pot_int == 0:
		Max_Player_Pot_Size_of_All_Rounds_int = max(List_of_Player_Pot_Values_int_List)
		
	# Formatted Print of Final Round Number and Max Player Pot Size to console
	Final_Game_Results_Output_str = "Based on our analysis you would have played {:,} Rounds before running out of money. Your pot reached a maximum value of: {:,} dollars during the Lucky Seven Game Analysis".format(Round_Number_int,Max_Player_Pot_Size_of_All_Rounds_int )
	print (Final_Game_Results_Output_str)
	
	'''ask player whether or not to play game again. if yes: reset all non-constant variables and Game Status to zero,null, or none, continue at beginning of while loop otherwise print farewell message and end program'''
	Play_Again_str = input("Would you like to run the Lucky Seven Game Analysis again?  yes or no:")
	if Play_Again_str == "yes":
		Game_Status_bool = True
		Players_Pot_int = 0
		Players_Pot_str = " " 
		Detailed_Game_Output_str = " "
		Detailed_Game_Output_bool = None
		Round_Number_int = 0
		Dice_Rolled_A_int = 0
		Dice_Rolled_B_int = 0
		Round_Payout_int = 0
		List_of_Player_Pot_Values_int_List = []
		Detailed_Output_str = " "
		Max_Player_Pot_Size_of_All_Rounds_int = 0
		Final_Game_Results_Output_str = " "
		freememory = gc.collect() #free up memory for continue use of the program
	else:
		Game_Status_bool = False
		
else:
	print (Farewell_Message_str)

