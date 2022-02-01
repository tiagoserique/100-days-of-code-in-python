import pandas


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word_input = input("Enter a word: ")

phonetic_code_words = [nato_data_dict[letter.upper()] for letter in word_input]

print(phonetic_code_words)
