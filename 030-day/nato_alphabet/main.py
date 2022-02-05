from numpy import False_
import pandas


nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

def generate_phonetic():
	try:
		word_input = input("Enter a word: ")
		output_list = [nato_data_dict[letter.upper()] for letter in word_input]
		
	except KeyError:
		print("Sorry, only letters in the alphabet please")
		generate_phonetic()

	else:
		print(output_list)


generate_phonetic()