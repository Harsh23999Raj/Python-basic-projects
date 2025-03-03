import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        
        if user_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice, please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        print("-" * 30)

if __name__ == "__main__":
    main()
