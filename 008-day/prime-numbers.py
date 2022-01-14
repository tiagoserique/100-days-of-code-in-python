#Write your code below this line 👇
import math

def prime_checker(number):
    prime = 1
    for n in range(2, math.ceil((number)/2) + 1):
        if ( number % n == 0 ):
            prime = 0
    
    if ( prime ):
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
