from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 
'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
	end_text = ""

	if ( cipher_direction == "decode" ):
		shift_amount *= -1

	for char in start_text:
		if ( char in alphabet ):
			position = alphabet.index(char)
			new_position = position + shift_amount
			end_text += alphabet[new_position]
		else:
			end_text += char
	
	print(f"Here's the {cipher_direction}d result: {end_text}")



print(logo)

continue_program = True

while ( continue_program ):

	direction = input("Type 'encode' to encrypt or 'decode' to decrypt a message: \n")
	text = input("Type the message: \n")
	shift = int(input("Type the shift number: \n"))

	if ( shift > 26 ):
		shift %= 26

	caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

	restart = input("Do you want to restart the program? 'yes' or 'no'? \n")
	if ( restart == "no" ):
		continue_program = False
		print("See you later!")