import random 

options = ["rock", "paper", "scissors"]

while True:
    print("\n1. Rock\n2. Paper\n3. Scissors\n")
    
    user_choice = int(input("Enter your choice (1-3) or 0 to exit: "))

    if user_choice == 0:
        print("Thank you for playing! Goodbye.")
        break
    elif user_choice == 1:
        user_choice = "rock"
    elif user_choice == 2:
        user_choice = "paper"
    elif user_choice == 3:
        user_choice = "scissors"
    else:
        print("Invalid choice! Please enter a number between 1 and 3.")
        continue

    computer_choice = random.choice(options)

    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("Result: You won!")
    else:
        print("Result: You lost.")
