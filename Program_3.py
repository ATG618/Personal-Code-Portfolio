#CS 101
#Program 3
#Alfred Harris
#ajhyr9@mail.umkc.edu
#Problem:
#Create a program that allows a user to play a game of rock-paper-scissors with
#the program. The program should be able to participate the moves of the user
#based on the previous moves the user has made. 
#Algorithm:
#1.	Prompt user with a welcome message, ask whether or not the user would like to play RSP Extreme v1.0 
#	a.	If user input is y or yes: set game status to True, and continue running program 
#	b.	If user input is n or no: set game status to False, and exit program 
#2.	Prompt user with help message, ask user to choose a weapon of choice, run function that selects weapon for computer.
#	a.	If user input is invalid: prompt user with a error message and ask for #input again.
#	b.	If user input is h or H or help: print help message.
#	c.	Function must choose computer weapon based on previous input by 
#	the user, and the weapon that is likely to win based on the most 
#	effective strategy.
#	d.	If user chooses q or Q or Quit: print total rounds played, player #rounds won,  computer rounds won, rounds tied,  player use of rock, player #use of paper, player use of scissors, and a farewell message. set game #status equal to False
#3.	Run function that determines winner based on game rules, print message #declaring round winner.
#	a.	Game rules: rock beats scissor, scissor beats paper, and paper beats #rock
#4.	While game status is set equal to True, continue running algorithm steps #1-3.
#	a.	Otherwise: exit program 

import time, random

#Initial Variables:
Welcome_Message_str = ''' Ming's RSP Ultra 
The World's First Super AI Rock Paper Scissors Game
Face Ming in a face off of world ending proportions!'''
prompt_to_play_msg_str = "Would you like to play Ming's RSP Ultra? Enter yes or no: "
prompt_to_play_valid_input_list = ['yes', 'y', 'no', 'n']
game_status_str = " "
game_status_bool = False
prompt_to_choose_weapon_msg_str =   "Enter h for help" + "\n" +"Choose your weapon: "
prompt_to_choose_weapon_valid_input_list = ['h','help','r','p','s','q','quit']
weapon_choice_weapons_only_list = [ 'r','s','p']
weapon_choice_user_str = " "
help_message_str = '''
The following are valid weapon choices: 
	h or help - generates help choices 
	r - rock weapon
	p - paper weapon
	s - scissors weapon 
	q or quit - quit game

How to Win:
	Rock(r) - Rock vs. Scissors -> Rock Wins
	Scissors(s) - Scissors vs. Papers -> Scissors Wins
	Paper(p) - Paper vs. Rock -> Paper Wins
	Any Weapon () - Weapon vs Same Weapon -> Draw Round
'''
prev_user_weapon_choices_tuple = None
choice_one_str = " "
choice_two_str = " "
choice_three_str = " " 
ming_weapon_str = " "
round_winner_str = " "
weapon_rock_use_int = 0 
weapon_paper_use_int = 0
weapon_scissors_use_int = 0
round_number_int = 0 
player_rounds_won_int = 0
ming_rounds_won_int = 0
tie_rounds_int = 0

# print welcome message, run function that prompts for valid input 
def prompt_for_valid_input (userinput_str, userinput_message_str, valid_input_list):
	'''this function prompts and checks user input for validity from list \
	asks for user input while input is not in valid input list print error message and ask for new input'''
	userinput_str = input (userinput_message_str)
	while userinput_str not in valid_input_list: #compare user input against list
		print ("Error. Invalid Input. Please try again")
		userinput_str = input (userinput_message_str)
		continue
	return userinput_str

#print welcome message and run function, strip space after return string
print (Welcome_Message_str)

game_status_str = prompt_for_valid_input(
game_status_str,
prompt_to_play_msg_str, 
prompt_to_play_valid_input_list
)

game_status_str.strip(" ")

while True:

#set game status based on input
	if game_status_str == "yes" or game_status_str == "y":
		game_status_bool = True
	elif game_status_str == "no" or game_status_str == "n":
		game_status_bool = False
		print ("Your Leaving so Soon? Too Bad! Thanks for Playing ")
		break


#Prompt user with help message, ask user to choose a weapon of choice, run function that validates user input.
	weapon_choice_user_str = prompt_for_valid_input (
	weapon_choice_user_str,
	prompt_to_choose_weapon_msg_str,
	prompt_to_choose_weapon_valid_input_list
	)
#prompt user with help message and ask user to choose weapon again. 
	while weapon_choice_user_str == 'h' or weapon_choice_user_str == 'help':
		print (help_message_str)
		weapon_choice_user_str = prompt_for_valid_input (
			weapon_choice_user_str,
			prompt_to_choose_weapon_msg_str,
			prompt_to_choose_weapon_valid_input_list
			)
		continue



#if user chose an actual weapon add the weapon choice to a tuple of previous choices, assign
#each value in the tuple of previous choices a variable, increment variables based on weapon use
	if weapon_choice_user_str in weapon_choice_weapons_only_list:
		if weapon_choice_user_str == "r":
			weapon_rock_use_int += 1
		elif weapon_choice_user_str == "p":
			weapon_paper_use_int += 1
		elif weapon_choice_user_str == "s":
			weapon_scissors_use_int += 1
		
		if len(weapon_choice_weapons_only_list) < 3:
			prev_user_weapon_choices_tuple = prev_user_weapon_choices_tuple + (weapon_choice_user_str,)
			choice_one_str, choice_two_str, choice_three_str = prev_user_weapon_choices_tuple

#run function that choose ming's weapon based on previous input by the user and strategy. 
	def weapon_choice_ming(choice_one_str, choice_two_str, choice_three_str): 
		'''determines weapon for ming by using player's previous choices'''
		def random_weapon_gen():
			'''assigns weight to each weapon, generates random weapon from weighted choices'''
		weighted_weapon_choices_list = [('r',4),('p',3),('s',3)]
		population = [val for val, count in weighted_weapon_choices_list for i in range(count)]
		random_weapon_str = random.choice(population)
		return random_weapon_str

	#strategy 1: player chooses same weapon as last round, run function to determine winning weapon and assign to ming 
		if choice_one_str == choice_two_str and choice_one_str == choice_two_str:
			#set ming's weapon to winning value for choice_one again
			def determine_winning_weapon(player_weapon_str):
				if player_weapon_str == "r":
					winning_weapon_str = "p"
				elif player_weapon_str == "p":
					winning_weapon_str = "s"
				elif player_weapon_str == "s":
					winning_weapon_str = "r"
				return winning_weapon_str
			ming_weapon_str = determine_winning_weapon(choice_one_str)
			return ming_weapon_str 
	#strategy 2: player chooses different weapon each round, run function to generate random weapon for ming from weighted list
		elif choice_one_str != choice_two_str and choice_one_str != choice_three_str:
			ming_weapon_str = random_weapon_gen(ming_weapon_str)
			return ming_weapon_str 


	def determine_round_winner(player_weapon_str, ming_weapon_str):
		'''function that determines round winner based on game rules'''
		if player_weapon_str == "r" and ming_weapon_str != "p" and ming_weapon_str != "r":
			round_winner_str = "player"
		elif player_weapon_str == "p" and ming_weapon_str != "s" and ming_weapon_str != "p" :
			round_winner_str = "player"
		elif player_weapon_str == "s" and ming_weapon_str != "r" and ming_weapon_str != "s":
			round_winner_str = "player"
		elif player_weapon_str == ming_weapon_str:
			round_winner_str = "tie"
		else:
			round_winner_str = "ming"
		return round_winner_str

	#run weapon choice function for ming and assign to variable
	ming_weapon_str = weapon_choice_ming(choice_one_str, choice_two_str, choice_three_str)
	#run function to determin round winner and assign round winner to variable
	round_winner_str = determine_round_winner(weapon_choice_user_str,ming_weapon_str)
	round_number_int += 1
	
	weapon_choices_str = '''You chose {:} and Ming chose {:}'''.format(weapon_choice_user_str, ming_weapon_str)
	print (weapon_choices_str)
	#if player wins, increment play stats, if ming wins, increment ming stats, otherwise increment tie rounds stats, print message for each outcome
	if round_winner_str == "player":
		player_rounds_won_int += 1
		print ('''Wow You won this round! 
Ming has felt the shame of defeat 
and seeks vengeance in the next round!''')
	elif round_winner_str == "ming":
		ming_rounds_won_int += 1
		print ('''You were defeated this round!
Give up! Ming cannot be defeated...''')
	elif round_winner_str == "tie":
		tie_rounds_int += 1
		print ('''Tie Round!
Ming has reaccessed his strategy
and is ready for another round''')

	# if game status is set to false print final game stats and end program
	#while user chooses to quit game run function to print game stats and set game status to false
	if weapon_choice_user_str == 'q' or weapon_choice_user_str == 'quit':
		game_status_bool = False
		Final_Game_Results_Output_str = '''Your attempt at victory, though futile, was valiant.
You played a total of {:,} Rounds  
You won a pitiful {:,} rounds during the game
Ming defeated you with ease {:,} times before you fled 
like a coward with your tail betweeen your legs.
You used rock {:,} times
You used paper {:,} times
You used scissor {:,} times

Thanks for playing!
'''.format(round_number_int,player_rounds_won_int,ming_rounds_won_int,weapon_rock_use_int, weapon_paper_use_int, weapon_scissors_use_int)
		print (Final_Game_Results_Output_str)
		break
