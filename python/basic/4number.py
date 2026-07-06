#import module like random 
import random

#integer number between 1 to 10
""" num1 = random.randint(1, 50)
print(f"The value of the random number is {num1} and the type is {type(num1)}") """

#float number between 1 to 1
""" num2 = random.uniform(1, 50)
print(f"The value of the random float number is {num2} and the type is {type(num2)}") """

#complex number between 1 to 10
""" num3 = complex(random.randint(1, 50), random.randint(1, 50))
print(f"The value of the random complex number is {num3} and the type is {type(num3)}") """

#Project 1: Guess the Random Int Number between 1 to 100 ⭐ (Beginner)
#Objective

#The computer generates a random int number , and the user has to guess it.
""" secret_number = random.randint(1, 100)
user_guess = int(input("Guess the int number between 1 to 100: "))

if user_guess == secret_number:
    print("Congratulations! You guessed the correct number.")
else:
    print("Sorry, thats not the correct number. The correct number is:", secret_number) """
