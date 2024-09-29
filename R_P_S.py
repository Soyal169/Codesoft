import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    options = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    
    while True:
        # User input
        user_choice = input("Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
        if user_choice == 'exit':
            break
        
        if user_choice not in options:
            print("Invalid choice. Please choose again.")
            continue
        
        # Computer's random choice
        computer_choice = random.choice(options)
        
        # Display choices
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        # Display scores
        print(f"Score -> You: {user_score}, Computer: {computer_score}")
        
        # Ask if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("Thanks for playing!")

# Run the game
play_game()
