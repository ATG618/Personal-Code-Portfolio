#CS 101
#Program 1
#Alfred Harris
#ajhyr9@mail.umkc.edu
#Problem: 
# 	Determine the total amount of pasta(in oz.)required for the large spaghetti 
#	party based on the number of attendees of varying type provided by the user.
#Algorithm: 
#	1. Prompt for user input for number of adults, number of students, and 
#		number of children that will attend the large spaghetti party.
# 	2. Convert user input for number of adults, number of students, and number of 
# 		children to integer data type
#   3. Compute total amount of pasta needed for large spaghetti party 
#       (where: Adult serving size of pasta is 8 ounces, Student serving size of 
#       pasta is 12 ounces, Children serving size of pasta is 4 ounces, and 
#       the Total Pasta required =(# of adults attending * adult serving size) +
#                              (# of students attending * student serving size) +        
#                               (# of children attedning * child serving size) 


"""Prompt for user input and assign that input to variable, and convert given 
input to integer data type"""  

adults_attending = input ("How many adults are attending your spaghetti party?")
adults_attending_int = int(adults_attending)

students_attending = input ("How many students are attending your spaghetti party?")
students_attending_int = int(students_attending)

children_attending = input ("How many children are attending your spaghetti party?")
children_attending_int = int(children_attending)

# assigns serving sizes of pasta for each type person to variable 
adult_serving_size_int = 8
student_serving_size_int = 12
child_serving_size_int = 4

# compute and print to console the total amount of pasta needed for the party 
total_pasta_required_int = ((adults_attending_int * adult_serving_size_int)+
    (students_attending_int * student_serving_size_int)+ 
    (children_attending_int * child_serving_size_int ))
print ("You will need a total of",total_pasta_required_int, \
    "ounces of pasta for your large spaghetti party!")
