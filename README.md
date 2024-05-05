## IIT Module - Introduction to programming coursework
# LifeScoreChallenge
Terminal based word game: Number score challenge

# Number Fighting Game

This is a simple text-based game where the player fights against random numbers to survive. The player's objective is to survive for 20 attempts by choosing numbers wisely.

## How to Play

1. Run the script.
2. Enter your name as "DON" when prompted.
3. Choose numbers to fight with.
4. Survive for 20 attempts to win the game.

## Game Rules

- You have to fight against random numbers.
- If you choose a number not within the given range, you lose.
- If the number you choose is less than or equal to your life score, you survive and gain that number's value to your life score.
- If the number you choose is greater than your life score, you lose.
- You win the game if you survive all 20 attempts.

## Files

- `YYYY_MM_DD_HH_MM_SS_ffffff.txt`: This file contains the game history and information.

## How to Run

1. Install Python on your system if you haven't already.
2. Copy the script to your local machine.
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is saved.
5. Run the script by typing `python script_name.py` and pressing Enter.

## Sample Output

Enter your name (as DON): DON

Attempt: 1
DON's life score is: 29
Numbers to fight with: [26, 67, 85, 93, 38]
Select a number to fight: 26
You fought the number 26 successfully!
Your updated Life Score is: 55

Attempt: 2
DON's life score is: 55
Numbers to fight with: [56, 72, 23, 37, 81]
Select a number to fight: 72
The number 72 killed you!! RIP

Game status
Player Name: DON
Total attempts: 2
Final score: 55
Oh no you were defeated


import random
import datetime

# Game logic code
# ...
