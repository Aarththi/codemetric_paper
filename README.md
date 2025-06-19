# codemetric_paper
Task 5 – Develop a Rock-Paper-Scissors Game
Goal: Build a Python console game where the user plays Rock-Paper-Scissors against the computer, using random generation, conditionals, and input validation.

✅ Features & Requirements:
Generate computer’s choice using random.choice()

Accept valid user input from predefined choices

Determine winner with if-elif-else conditions

Loop until the user chooses to exit

Input validation for wrong entries

 Python Code:
python
Copy
Edit
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
📚 Detailed Explanation:
🔁 Game Loop (main())
Runs until the user types "exit"

Calls get_user_choice() and get_computer_choice()

Prints the choices and the result using determine_winner()

🎲 Random Choice
random.choice(['rock', 'paper', 'scissors']) simulates the computer's play

✅ Input Validation
User can only enter one of the valid choices: "rock", "paper", "scissors", "exit"

If invalid input is entered, the loop re-prompts

🧠 Winner Logic
Uses if-elif structure to compare moves and decide the result

Covers all win/lose/tie scenarios

🧼 Entry-Point Check
if __name__ == "__main__" ensures main() runs only if script is directly executed

 Example Run:
pgsql
Copy
Edit
🎮 Welcome to Rock-Paper-Scissors!
Enter rock, paper, scissors, or 'exit' to quit: rock

You chose: rock
Computer chose: scissors
You win! 🎉
------------------------------
Enter rock, paper, scissors, or 'exit' to quit: paper

You chose: paper
Computer chose: rock
You win! 🎉
------------------------------
Enter rock, paper, scissors, or 'exit' to quit: fire
Invalid choice. Try again.
Enter rock, paper, scissors, or 'exit' to quit: exit
Thanks for playing. Goodbye! 👋

What You Learn:
Randomization with Python’s random module

Control flow with if-elif-else statements

Input validation using lists and loops

Encapsulation with functions for cleaner code

Game logic implementation with minimal code

Replay loop and clean exits
