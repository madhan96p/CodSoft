import random

def get_user_choice():
    print("\nChoose your weapon:")
    print("1. Rock 🪨")
    print("2. Paper 📄")
    print("3. Scissors ✂️")
    choice = input("Enter 1, 2 or 3: ")
    options = {"1": "rock", "2": "paper", "3": "scissors"}
    return options.get(choice, None)

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user} | Computer chose: {computer}")
    if winner == "tie":
        print("It's a TIE! 🤝")
    elif winner == "user":
        print("You WIN! 🎉")
    else:
        print("You LOSE! 😢")

def play_game():
    user_score = 0
    computer_score = 0
    round_num = 1

    print("🎮 Welcome to Rock-Paper-Scissors Game!")
    print("======================================")

    while True:
        print(f"\n--- Round {round_num} ---")
        user_choice = get_user_choice()
        if not user_choice:
            print("Invalid input! Please enter 1, 2, or 3.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break
        round_num += 1

if __name__ == "__main__":
    play_game()
