from art import logo
import random
import os


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_guess(guess, answer):
	if ( guess > answer ):
		print("Too High")

	elif ( guess < answer ):
		print("Too Low")

	else:
		print(f"\nYou got it! The answer was {answer}")


def set_difficulty():
	if ( input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy' ):
		return EASY_LEVEL_TURNS

	else:
		return HARD_LEVEL_TURNS


os.system('clear')
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

answer = random.randint(1, 100)

number_of_attempts_remaining = set_difficulty()

is_game_over = False
while not( is_game_over ):
	print(f"\nYou have {number_of_attempts_remaining} attempts remaining to guess the number.")
	
	guess = int(input("Make a guess: "))

	number_of_attempts_remaining -= 1
	
	check_guess(guess, answer)
	if ( guess == answer ):
		is_game_over = True
		
	elif ( number_of_attempts_remaining == 0 ):
		is_game_over = True
		print("\nYou've run out of guessed, you lose")

