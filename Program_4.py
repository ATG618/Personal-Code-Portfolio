#CS 101
#Program 3
#Alfred Harris
#ajhyr9@mail.umkc.edu
#Problem:
#Create a program that allows a user to play a game of rock-paper-scissors with
#the program. The program should be able to participate the moves of the user
#based on the previous moves the user has made. 
#Algorithm:
#1.	Prompt user to input the name of the file to be scrambled. 
#2.	Run function that takes user input as parameter, opens file with the 
#	matching name, and read file converting each line in text from file into 
#	a list of strings. Assign list of strings to a list variable
#		a.	If file name is not found, prompt error message, and prompt for 
#			input again. 
#3.	Run outer function that takes a string as a parameter and splits strings 
#into a list of words, and assigns list of words to a list of words variable.
#	a.	Iterate through list of string variable to run function on each 
#		element in lists of string variable.
#4.	Run inner function that takes a word string variable from outer function 
#	as a parameter. If word string variable is not only alphabetic characters. 
#	Strip non-alphabetic elements from string.   
#	a.	If word string variable has length less than 3 characters in length, 
#	return the unmodified word string variable from outer function text saving 
#	to a temporary file.
#	b.	Else if word string variable is greater than 3 elements in length. 
#	Strip elements in word string variable (excluding the first and last element 
#	of word string variable). Run random method on stripped element list. 
#	Replace original elements with the randomized stripped elements 
#	(still excluding the first and last element of the word string variable).  
#	c.	Return modified text from outer function text saving to a temporary file. 
#5.	Print all text from temporary file.

#Step 1: Prompt User to input the name of the file to be scrambled.(Tested)
userinput_str = ""
userinput_message_str = "Enter name of file to be scrambled: "
userinput_str = input(userinput_message_str)


#Take file name from user and to open file with the name of the valid input
while True:
	try:
		InputFile = open(userinput_str, "r")
		break
	except FileNotFoundError: #when file not found print message and continue loop
		print ("Error. Invalid Input. Please try again")
		continue

#Step 2: iterate through for loop splitting lines of text into a list of words. Assign to variable.
List_of_words_list = []
newline = []
for line in InputFile:
	print (line)
	newline = line.split()
	List_of_words_list.append(newline)


def reverse_word(string):
	'''Receives word string as parameter, reverse order of letters excluding the beginning and ending letter of the word string '''
	status = None
	period = '.'
	comma = ','
	reversed_string = ""
	#if length of string is less than 3 characters or is numeric, simply return reversed_string to program
	if len(string) <= 3 or str(string).isnumeric() == True:
		return string
	#otherwise run the remainder of the function
	else:
		#if there is a period or comma inside string. strip period/comma from string and update status variable
		if period in string:
			string = string.strip(period)
			status = "period"
		elif comma in string:
			string = string.strip(comma)
			status = "comma"

		#convert string to a list
		string_list = list(string)
		
		#variables for beginning and ending letters of word string
		beg = 0
		end = -1

		#splice letters from string excluding beg and end locations
		spliced_string = string_list[(beg + 1):(end)]

		#reverse the order of the spliced string
		spliced_string.reverse()

		#using join str method, convert the reversed spliced string back to str data type
		spliced_string = "".join(spliced_string)

		#convert beginning and ending letters of unmodified list back to str and concatenate with reversed str
		reversed_string = str(string_list[beg])+spliced_string+str(string_list[end])
		
		#if status was change to period/comma concatenate period/comma respectively to string
		if status == "period":
			reversed_string = reversed_string + period
		elif status == "comma":
			reversed_string = reversed_string + comma
		return reversed_string

#Step 3:Iterate through for loop, run function on each element in list of words variable.
Reversed_List_of_words_List = []
word = []
for line in List_of_words_list:
	for word in line:
		modified_word = reverse_word(word)
		Reversed_List_of_words_List.append(modified_word)
  
def join_text_with_space(list):
	'''Join text from list into one string variable'''
	string = " ".join(list)
	return string
#Step 4: run function that joins modified list of words back to one string  
Modified_String = ""	
Modified_String = join_text_with_space(Reversed_List_of_words_List)

#save modified text to a temporary file
with open("temp_file.txt", 'w') as OutputFile:
	OutputFile.write(Modified_String)

#open temporary file and print text from file to console
with open("temp_file.txt", 'r') as OutputFile:	
	for line in OutputFile:
		print (line)


