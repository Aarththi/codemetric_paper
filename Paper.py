import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    valid_choices = ['rock', 'paper', 'scissors', 'exit']
    while True:
        choice = input("Enter rock, paper, scissors, or 'exit' to quit: ").lower()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Try again.")

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')
    ):
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

def main():
    print("\n🎮 Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        if user_choice == 'exit':
            print("Thanks for playing. Goodbye! 👋")
            break
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        print("-" * 30)

if __name__ == "__main__":
    main()
