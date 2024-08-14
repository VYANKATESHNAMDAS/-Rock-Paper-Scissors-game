import random
import os
from setup.sprint import sprint
from setup.colors import c, r, ran, lr, lc, lg, g, ly, y
from setup.banner import banner, banner2, clear


# Function to determine the winner
def game_win(comp, you):
    if comp == you:
        return None
    elif (comp == 'r' and you == 's') or (comp == 'p' and you == 'r') or (comp == 's' and you == 'p'):
        return False
    else:
        return True

# Main game loop
def play_game():
    os.system("clear")
    banner()
    options = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    n = 3
    for _ in range(n):
        print("ROCK (r) , PAPER (p) , SCISSORS (s) = ? ")
        
        # Randomly choose for the computer
        comp = random.choice(['r', 'p', 's'])
        
        # User's turn
        you = input("YOUR TURN! PRESS: ROCK (r) , PAPER (p) , SCISSORS (s) = ").lower()
        while you not in options:
            you = input("Invalid input. Please press: ROCK (r) , PAPER (p) , SCISSORS (s) = ").lower()
        
        # Determine the winner
        result = game_win(comp, you)
        
        # Print results
        print(f"COMPUTER CHOSE: {options[comp]}")
        if result is None:
            print("GAME TIED!")
        elif result:
            print("YOU WIN!")
        else:
            print("YOU LOSE!")
        
        # Ask if the user wants to play again
        if _ < n - 1:
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                break

if __name__ == "__main__":
    play_game()
