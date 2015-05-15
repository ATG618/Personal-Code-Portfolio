import os.path, math

def clean_up(s):
	''' Return a version of string str in which all letters have been
	converted to lowercase and punctuation characters have been stripped 
	from both ends. Inner punctuation is left untouched. '''
	
	punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
	result = s.lower().strip(punctuation)
	return result

def word(clean_text):
	'''Return word based on program definition. '''
	list_of_words = list()
	average_word_length = 0
	#WORD: for each line in text, split by space, and to list of words
	for line in text:
		wordlist = line.split()
		for word in wordlist:
			if word != "":
				list_of_words.append(word)
	return list

def average_word_length(text):
	''' Return the average length of all words in text. Do not
	include surrounding punctuation in words. 
	text is a non-empty list of strings each ending in \n.
	At least one line in text contains a word.'''
	
	# To do: Replace this function's body to meet its specification.
	clean_text_str = ""
	clean_text_str = clean_up(text)
	
	#run word function
	list_of_words = list()
	list_of_words = word(clean_text_str)
	
	list_of_wordlengths = list()
	#for each word in list of words, add length of each to list of word lengths
	for word in list_of_words:
		 list_of_wordlength.append(len(word))
	
	#calculate average word length for entire text
	num = float(sum(list_of_wordlength))
	denom = float(len(list_of_wordlength))
	average_word_length = num/denom 
	
	return average_word_length

def type_token_ratio(text):
	''' Return the type token ratio (TTR) for this text.
	TTR is the number of different words divided by the total number of words.
	text is a non-empty list of strings each ending in \n.
	At least one line in text contains a word. '''
  
	#Clean text received as parameter
	clean_text_str = ""
	clean_text_str = clean_up(text)
	
	#run word function on cleaned text
	list_of_words = list()
	list_of_words = word(text)
	
	#compute total number of words
	total_words_int = 0
	totalwords_int = len(list_of_words)
	
	#for every word in list, count number of unique words in list
	list_of_uniquewords = list()
	for word in list_of_words:
		if word not in list_of_uniquewords:
			list_of_uniquewords.append(word)
	uniquewords_count_int = len(list_of_uniquewords) 
	
	#compute type token ratio from calculated values
	type_token_ratio_float = float(uniquewords_count_int)/float(totalwords_int)
	return type_token_ratio_float
	

def hapax_legomana_ratio(text):
	''' Return the hapax_legomana ratio for this text.
	This ratio is the number of words that occur exactly once divided
	by the total number of words.
	text is a list of strings each ending in \n.
	At least one line in text contains a word.'''
 
	#Clean text received as parameter
	clean_text_str = ""
	clean_text_str = clean_up(text)
	
	#run word function on cleaned text
	list_of_words = list()
	list_of_words = word(text)
	
	#compute total number of words
	total_words_int = 0
	total_words_int = len(list_of_words)
	
	#for every word in list, if word appears only once add to words appearing once list 
	words_appearing_once_list = list()
	for word in list_of_words:
		if list_of_words.count(word) == 1:
			words_appearing_once_list.append(word)
	
	#count of words appearing once
	words_appearing_once_count_float = len(words_appearing_once_list) 
	
	#compute hapax legomana ratio from calculated values
	hapax_legomanaratio_float = float(words_appearing_once_count_float)/float(totalwords_int)
	
	return hapax_legomanaratio_float


def split_on_separators(original, separators):
	''' Return a list of non-empty, non-blank strings from the original string
	determined by splitting the string on any of the separators.
	separators is a string of single-character separators.'''
	
	# To do: Complete this function's body to meet its specification.
	# You are not required to keep the two lines below but you may find
	# them helpful. (Hint)
	
	#Clean text received as parameter
	clean_text_str = ""
	clean_text_str = clean_up(text)
	
	
	result = [original]
	return result
				
	
def average_sentence_length(text):
	''' Return the average number of words per sentence in text.
	text is guaranteed to have at least one sentence.
	Terminating punctuation defined as !?.
	A sentence is defined as a non-empty string of non-terminating
	punctuation surrounded by terminating punctuation
	or beginning or end of file. '''
	
	# To do: Replace this function's body to meet its specification.
	return 1
	

def avg_sentence_complexity(text):
	'''Return the average number of phrases per sentence.
	Terminating punctuation defined as !?.
	A sentence is defined as a non-empty string of non-terminating
	punctuation surrounded by terminating punctuation
	or beginning or end of file.
	Phrases are substrings of a sentences separated by
	one or more of the following delimiters ,;: '''
	
	# To do: Replace this function's body to meet its specification.
	return 1.0
	
	
def get_valid_filename(prompt):
	'''Use prompt (a string) to ask the user to type the name of a file. If
	the file does not exist, keep asking until they give a valid filename.
	Return the name of that file.'''
	#Complete this function's body to meet its specification.
	file_status_bool = True
	while file_status_bool == True:
		try:
			filename = input(prompt)
			open(filename, "r")
			return filename
			file_status_bool = False
		except FileNotFoundError:
			print ("That file does not exist.")
			filename = input(prompt)
	# Uncomment and use this statement as many times as needed for input:
	# Uncomment and use this statement as many times as needed for output:
	# Do not use any other input or output statements in this function.
	
def read_directory_name(prompt):
	'''Use prompt (a string) to ask the user to type the name of a directory. If
	the directory does not exist, keep asking until they give a valid directory.
	'''
	
	# To do: Complete this function's body to meet its specification.
	dirname = input(prompt)
	return dirname

	# Uncomment and use this statement as many times as needed for input:
	# dirname = input(prompt)
	# Uncomment and use this statement as many times as needed for output:
	# print "That directory does not exist."
	# Do not use any other input or output statements in this function.
	
	
def compare_signatures(sig1, sig2, weight):
	'''Return a non-negative real number indicating the similarity of two 
	linguistic signatures. The smaller the number the more similar the 
	signatures. Zero indicates identical signatures.
	sig1 and sig2 are 6 element lists with the following elements
	0  : author name (a string)
	1  : average word length (float)
	2  : TTR (float)
	3  : Hapax Legomana Ratio (float)
	4  : average sentence length (float)
	5  : average sentence complexity (float)
	weight is a list of multiplicative weights to apply to each
	linguistic feature. weight[0] is ignored.
	'''
	
	# To do: Replace this function's body to meet its specification.
	return  0.0
	

def read_signature(filename):
	'''Read a linguistic signature from filename and return it as 
	list of features. '''
	
	file = open(filename, 'r')
	# the first feature is a string so it doesn't need casting to float
	result = [file.readline()]
	# all remaining features are real numbers
	for line in file:
		result.append(float(line.strip()))
	return result
		

if __name__ == '__main__':
	prompt = 'enter the name of the file with unknown author:'
	mystery_filename = get_valid_filename(prompt)

	# readlines gives us the file as a list of strings each ending in '\n'
	text = open(mystery_filename, 'r').read()
	#text.close() 
	
	
	# calculate the signature for the mystery file
	mystery_signature = [mystery_filename]
	mystery_signature.append(average_word_length(text))
	mystery_signature.append(type_token_ratio(text))
	mystery_signature.append(hapax_legomana_ratio(text))
	mystery_signature.append(average_sentence_length(text))
	mystery_signature.append(avg_sentence_complexity(text))
	
	weights = [0, 11, 33, 50, 0.4, 4]
	
	prompt = 'enter the path to the directory of signature files: '
	dir = read_directory_name(prompt)
	# every file in this directory must be a linguistic signature
	files = os.listdir(dir)

	# we will assume that there is at least one signature in that directory
	this_file = files[0]
	signature = read_signature('{} {}'.format(dir,this_file)))
	best_score = compare_signatures(mystery_signature, signature, weights)
	best_author = signature[0]
	for this_file in files[1:]:
		signature = read_signature('{} {}'.format(dir,this_file)))
		score = compare_signatures(mystery_signature, signature, weights)
		if score < best_score:
			best_score = score
			best_author = signature[0]
	print( "best author match: {} with score {}".format(best_author, best_score))
	
	
