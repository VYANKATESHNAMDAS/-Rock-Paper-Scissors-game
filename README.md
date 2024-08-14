# Rock-Paper-Scissors

This repository contains an enhanced version of the classic Rock-Paper-Scissors game implemented in Python. The game features a simple command-line interface, with a colorful banner and user prompts to make the experience more engaging.

## Features

- **Randomized Computer Choices:** The computer randomly selects Rock, Paper, or Scissors.
- **User-Friendly Interface:** The game includes a colorful banner and uses clear prompts for user interaction.
- **Input Validation:** The program ensures that only valid inputs are accepted from the user.
- **Best of Three:** The game is played over three rounds by default.
- **Customizable Colors and Banners:** The game leverages custom banners and color schemes for a more interactive experience.

## Requirements

- Python 3.x
- The `setup` directory with the following modules:
  - `sprint`
  - `colors`
  - `banner`

These modules should define the color schemes and banner designs for the game.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/rock-paper-scissors.git
    ```

2. Navigate to the project directory:

    ```bash
    cd rock-paper-scissors
    ```

3. Ensure that the `setup` directory and all required modules (`sprint`, `colors`, `banner`) are correctly placed within the project directory.

## Running the Game

1. Run the game script:

    ```bash
    python rock_paper_scissors.py
    ```

2. Follow the on-screen prompts to play the game.

## Customization

- **Banners:** Modify the `banner()` and `banner2()` functions in the `setup/banner.py` file to customize the game’s banners.
- **Colors:** Adjust color schemes in the `setup/colors.py` file to suit your preferences.
- **Game Rounds:** Change the number of rounds by modifying the `n` variable in the `play_game()` function.

## Example Output

```plaintext
***************
* ROCK-PAPER-SCISSORS *
***************

ROCK (r), PAPER (p), SCISSORS (s) = ? 
YOUR TURN! PRESS: ROCK (r), PAPER (p), SCISSORS (s) = r
COMPUTER CHOSE: Scissors
YOU WIN!

