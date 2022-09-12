"""
* Created By Miguel Gemio

* Date: 11/09/22
* time: 21:00
* Project Name: Exercise - Paper-rock-scissors
"""

# Let the computer select a random choice

# importing Random
import random

options = ["Paper", "Rock", "Scissors"]

# Get a Random Number
random_choice = random.randrange(0, 3)

# Get user option
print("Chose an option:\n1)Paper\n2)Rock\n3)Scissors")
user_choice = int(input("--> "))

# Get the String of the option
user_choice = options[user_choice - 1]
random_choice = options[random_choice]

# Print message of options selected 
print(f"You choose: {user_choice}")
print(f"PC choose: {random_choice}")
print("...")

# Print the resultsß
if random_choice == "Rock" and user_choice == "Paper":
    print("You Win, Paper wins Rock")
elif random_choice == "Paper" and user_choice == "Scissors":
    print("You Win, Scissors cuts Paper")
elif random_choice == "Scissors" and user_choice == "Rock":
    print("You Win, Rock wins Scissors")
if random_choice == "Paper" and user_choice == "Rock":
    print("You lose, Paper wins Rock")
elif random_choice == "Scissors" and user_choice == "Paper":
    print("You lose, Scissors cuts Paper")
elif random_choice == "Rock" and user_choice == "Scissors":
    print("You lose, Rock wins Scissors")
elif random_choice == user_choice:
    print("tie")