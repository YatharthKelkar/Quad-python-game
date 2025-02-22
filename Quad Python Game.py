import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

def dice_roll():
    print(f"You rolled a {random.randint(1, 6)}")

if __name__ == "__main__":
    while True:
        print("\nChoose a game:")
        print("1. Number Guessing Game")
        print("2. Rock Paper Scissors")
        print("3. Dice Roll")
        print("4. Exit")
        
        try:
            choice = int(input("Enter the number of the game you want to play: "))
            if choice == 1:
                number_guessing_game()
            elif choice == 2:
                rock_paper_scissors()
            elif choice == 3:
                dice_roll()
            elif choice == 4:
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")
