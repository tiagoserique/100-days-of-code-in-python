from game_data import data
from art import logo, vs
import random
import os


def format_data(celebrity):
	name 		= celebrity['name']
	description = celebrity['description']
	country 	= celebrity['country']
	
	return f"{name}, a {description}, from {country}"


def compare_celebrity(celebrity_a, celebrity_b):
	"""
		Compares two follower counters of two celebrities and the answer to the 
		question "who has more followers". Returns True if the player chooses 
		the right answer and False if he chooses the wrong answer.  
	"""
	answer = input("Who has more followers? Type 'A' or 'B': ").lower()
	
	a_followers = celebrity_a['follower_count']
	b_followers = celebrity_b['follower_count']

	if ( a_followers > b_followers ) and ( answer == 'a' ) \
	or ( a_followers < b_followers ) and ( answer == 'b' ):
		return True

	return False


def select_celebrity():
	"""
		randomly pick a celebrity from the data list
	"""
	return random.choice(data)


os.system('clear')
print(logo)

celebrity_a = select_celebrity()

score 			= 0
is_game_over 	= False
while not( is_game_over ):

	print(f"Compare A: {format_data(celebrity_a)}")
	
	print(vs)
	
	celebrity_b = select_celebrity()
	while ( celebrity_a == celebrity_b ):
		celebrity_b = select_celebrity()

	print(f"Compare B: {format_data(celebrity_b)}")
	
	is_right = compare_celebrity(celebrity_a, celebrity_b)
	if ( is_right ):
		celebrity_a = celebrity_b
		score += 1
		
		os.system('clear')
		print(logo)
		print(f"You're right! Current score: {score}")

	else:
		os.system('clear')
		print(logo)
		print(f"Sorry, that's wrong. Final score: {score}")
		is_game_over = True


