
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if ( size == 'S' ):
    final_value = 15

elif ( size == 'M' ):
    final_value = 20

else:
    final_value = 25

if ( add_pepperoni == 'Y' ):
    if ( size == 'S' ):
        final_value += 2
        
    else:
        final_value += 3

if ( extra_cheese == 'Y' ):
    final_value += 1

print(f"Your final bill is: ${final_value}.")
