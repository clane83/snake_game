
How to Run the Game
1. Install Python

Download Python from:
Python Official Website
Make sure Python is added to your system PATH during installation.

----------------------------

2. Download the Project Files

Make sure all files are in the same folder:

main.py
snake.py
food.py
score.py
data.txt

----------------------------

3. Run the Game

Open a terminal or command prompt in the project folder and run:

python main.py
Controls
Key	Action
Up Arrow	Move Up
Down Arrow	Move Down
Left Arrow	Move Left
Right Arrow	Move Right

----------------------------

Game Rules
Eat food to grow the snake and increase your score.
If the snake hits the wall:
The game resets
The score resets
The high score is saved
If the snake hits its own tail:
The game resets
The score resets

----------------------------

High Score System

The game saves the highest score in a file called:
data.txt

This allows the high score to persist even after closing the game.

----------------------------

Code Overview
main.py

Handles:

Screen setup
Game loop
Keyboard controls
Collision detection
snake.py

Contains the Snake class:

Snake creation
Snake movement
Snake growth
Direction handling
Reset logic
food.py

Contains the Food class:

Random food placement
Food appearance
score.py

Contains the Score class:

Score tracking
High score tracking
Scoreboard updates

----------------------------

Future Improvements

Possible upgrades for the project:
Add difficulty levels
Add sound effects
Add pause functionality
Add game over screen
Add colored snake segments
Add obstacles
Add start menu

----------------------------

Author

Created by Christina Lane