# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2

total1 = combined_names.lower().count('t') 
total1 += combined_names.lower().count('r')
total1 += combined_names.lower().count('u')
total1 += combined_names.lower().count('e')

total2 = combined_names.lower().count('l') 
total2 += combined_names.lower().count('o')
total2 += combined_names.lower().count('v')
total2 += combined_names.lower().count('e')

score = int(str(total1) + str (total2))

if ( score < 10 ) or ( score > 90 ):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif ( score > 40 ) and ( score < 50 ):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
