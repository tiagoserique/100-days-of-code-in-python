from art import logo
import random
import os


def calculate_score(hand):
    """
        Calculates the score of a hand of blackjack and return it.
        In case of a blackjack, then the value 0 is returned
    """
    score = sum(hand)
    
    if ( score == 21 ) and ( len(hand) == 2 ):
        return 0

    elif ( score > 21 ) and ( 11 in hand ):
        hand.remove(11)
        hand.append(1)

    return score


def deal_card():
    """
        Picks a card from the list of cards and then give it to the hand of the 
        player 
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def compare(player_score, computer_score):
    """
        Compares the player score and the computer score to say who win the game
    """
    if ( player_score == computer_score ):
        return "It's a drawn"

    elif ( computer_score == 0 ):
        return "Blackjack!!! You lose :("

    elif ( player_score == 0 ):
        return "Blackjack!!! You win :D"

    elif ( player_score > 21 ):
        return "You went over. You lose :/"

    elif ( computer_score > 21 ):
        return "Opponent went over. You win c:"

    else:
        if ( player_score > computer_score ):
            return "You win :3"

        else:
            return "You lose >_>"


def play_game():
    """
        The game of blackjack
    """
    print(logo)

    computer_hand = []
    player_hand   = []

    for _ in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    computer_score = calculate_score(computer_hand)

    is_end_game = False
    while not( is_end_game ):
        player_score = calculate_score(player_hand)

        print(f"    Your cards: {player_hand}")
        print(f"    Current score: {player_score}\n")
        print(f"    Computer first card: {computer_hand[0]}\n")

        if ( player_score == 0 ) or ( computer_score == 0 ) or ( player_score > 21 ):
            is_end_game = True

        else:
            player_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            
            if ( player_should_deal == 'y' ):
                player_hand.append(deal_card())

            else:
                is_end_game = True


    while ( computer_score != 0 ) and ( computer_score < 17 ):
            computer_hand.append(deal_card())
            computer_score = calculate_score(computer_hand)

    print(f"\n  Your final hand: {player_hand} | Computer final hand: {computer_hand}\n")
    print(f"  Your final score: {player_score} | Computer final score: {computer_score}\n")
    print("  " + compare(player_score, computer_score))




while ( input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y' ):
    os.system('clear')
    play_game()

