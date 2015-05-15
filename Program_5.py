#CS 101
#Program 5
#Alfred Harris
#ajhyr9@mail.umkc.edu
#Problem:
#Program will manipulate data from file concerning sunspot observation data 
#going back to 1818. Must produce a new file with data in a specific data. 
#Must produce average data from already produced file. Must produce a graph of
#the smoothed data, and estimate the next likely sun spot activity. 
#Algorithm:
#Step 1: Open file named "dailysunspots.txt" assign to Input File Variable
#Step 2: Iterate through for loop for each line in Input File 
#	a. Split line by space and assign to list variable
#	b. Iterate through a for loop for each column in list 
#		i. If length is equal to 8 and does not contain a period then assign to date variable 
#		ii. If length is equal to less than 3 then assign to sunspot variable. Increment count for sunspots
#Step 3: Iterate through for loop for list of date variables
#	a. Splice list of date variables into year and month. Disregard day data. Format of data is "YYYYMMDD"
#Step 4: Calculate average of sunspots by month using for loop iterating through one to 12
#	a. Divide list of supports by sunspot count
#Step 5: Write data to month file
#Step 6: Write file named "smooth.txt"
#	a. Calculate smooth value of average data for each month using formula:
#		(0.5*first_value + 0.5*last_value + all_values)


#Step 1: while status_bool is true, Open file named "dailysunspots.txt". 
#if file not found raise exception and print error message

filename = "dailysunspots.txt"
status_bool = True
while status_bool:
	try:
		InputFile = open(filename, "r")
		status_bool = False
	except FileNotFoundError: #when file not found print message and continue loop
		print ("Error. Invalid Input. Please try again")
	
		
#Step 2: Iterate through for loop for each line in Input File
CompleteFile_list = []
List_of_SplitLines = []
for line in InputFile:	
	newline = line.split()	#split string by space and assign to list variable
	List_of_SplitLines.append(newline)	#add list variable to 

#b. Iterate through a for loop for each column in list 
#	i. If length is equal to 8 and does not contain a period then assign to date variable 
#	ii. If length is equal to less than 3 then assign to sunspot variable. Increment count for sunspots	
period = "."
date_str = ""
sunspot_float = 0.0
sunspot_count = 0 
List_of_dates = []
date_year_int = 0
date_month_int = 0
List_of_SunspotRecords = list()
test = "20130112, 2013.001, 999"

class SunspotRecord(object):
	"""Record of Sunspot by Year and Month"""
	
	def __init__(self,year=0,month=0,sunspot=0.0):	#initializer
		self.date_year_int=year
		self.date_month_int=month
		self.sunspot_float=sunspot
		
	def update(self,year=0,month=0,sunspot=0.0):	#allows user to modify the attributes of a class instance
		if year:
			self.date_year_int = year
		if last:
			self.date_month_int = month
		if sunspot:
			self.sunspot_float = sunspot
			
	def __str__(self):	#string representation, for printing
		return "Year: {} Month: {} Sunspot Observed: {}".format\
			(self.date_year_int, self.date_month_int, self.sunspot_float)

			
for line in List_of_SplitLines: #iterate each line in list "20130112, 2013.001, 999"
	for column in line:	#iterate through each str in line	"20130112"/ "2013.001" / "55"
		#if the length of the column is equal to 8 and a period is not in column
		#convert column to str and assign column to a date variable
		if len(column) == 8 and period not in column:	#"20130112"
			date_str = str(column)						#"20130112"
			#Splice date variable into year, month, 
			#date variables, convert to int respectively, 
			#disregard day data
			date_year_int = int(date_str[0:4])				#2013
			date_month_int = int(date_str[4:6])
		#if the length of the column is less than or equal to 3
		#convert column to float and assign column to a sunspot variable
		if len(column) <= 3 and column != "999":		#"55"
			try:
				sunspot_float = float(column)				#55.0
			except ValueError:
				
		
		#create a classinstance of sunspotrecord matching date to sunspots
		sunspotrec = SunspotRecord(date_year_int,date_month_int,sunspot_float)
		List_of_SunspotRecords.append(sunspotrec) 
			
#Step 4: Calculate average of sunspots by month using for loop iterating through one to 12
#	a. Divide list of sunspots by sunspot count	
			
def Calculate_Average(masterlist):
	'''Receive list as paramater, calculate average of sunspots by month'''
	
	List_of_Months = [1,2,3,4,5,6,7,8,9,10,11,12]
	List_of_Years = list(range(1818,2014))
	sunspot_avg_num_float = 0.0
	sunspot_avg_denom_int = 0
	sunspot = 0
	List_of_Monthly_Averages = list()
	monthly_average = 0
	
	for record in masterlist:	
		#Retrieve variable attributes of sunspotrecord class instance from each record in list 
		current_year = record.date_year_int
		current_month = record.date_month_int
		current_sunspot = record.sunspot_float
		
		#iterate through for loop for each year and each month, 
		#calculating monthly averages and adding to list variable.
		for year in List_of_Years:
			for month in List_of_Months:
				if current_year == year and current_month == month: 
					sunspot_avg_num_float += current_sunspot
					sunspot_avg_denom_int += 1
					sunspot_avg_float = sunspot_avg_num_float/sunspot_avg_denom_int
					monthly_average = [current_year, current_month, sunspot_avg_float]
				List_of_Monthly_Averages.append(monthly_average)
	return 	List_of_Monthly_Averages

#Calculate Monthly Average using function, take list of sunspot records as parameter	
List_of_Monthly_Averages = Calculate_Average(List_of_SunspotRecords)
	
#Step 5: Write data to month file
def join_text_with_space(list):
	'''Join text from list into one string variable'''
	string = " ".join(list)
	return string

#create monthly file and run function that joins modified list of words back to one string  
Modified_String = ""
OutputFile = open("MONTHLY.txt",'w')
for line in List_of_Monthly_Averages:
	Modified_String = join_text_with_space(line)
	
	#save modified text to a file
	with open("MONTHLY.txt", 'a') as OutputFile:
		OutputFile.write(Modified_String)

#Step 6: Write file named "smooth.txt"
#	a. Calculate smooth value of average data for each month using formula:
#		(0.5*first_value + 0.5*last_value + all_values)

OutputFile = open("SMOOTH.txt",'w')
