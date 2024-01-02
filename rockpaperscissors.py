import random

game_names = ["rock", "paper", "scissors"]
print (game_names)

user_choice = int (input("What do you choose? Type 0 for Block 1, 1 for Paper and 2 for Scissors.\n"))
print (game_names[user_choice])

computer_choice = random.randint(0,2)
print(game_names[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > computer_choice :
    print("You win!")
elif user_choice < computer_choice :
    print("You lose!")
elif user_choice == computer_choice :
    print("You draw!")