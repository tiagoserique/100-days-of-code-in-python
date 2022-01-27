from os import clear
from art import logo 
#HINT: You can call clear() to clear the output in the console.


def who_is_the_winner(bidders_info):
    heighest_bid = 0
    for person in bidders_info:
        if ( bidders_info[person] > heighest_bid ):
            winner = person
            heighest_bid = bidders_info[person]
        
    print(f"The winner is {winner} with a bid of {heighest_bid}")


continue_bidding = True
print(logo)
bidders_info = {}

while ( continue_bidding ):
    name    = input("What's your name?\n")
    price   = int(input("What is your bid?\n$"))

    bidders_info[name] = price

    theres_another_person = input("Are there any other bidders? Type 'yes' or 'no'\n")

    if ( theres_another_person == 'yes' ):
        clear()

    if ( theres_another_person == 'no' ):
        clear()
        who_is_the_winner(bidders_info)
        continue_bidding = False
