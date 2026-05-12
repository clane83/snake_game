# Snake Game 🐍

A classic Snake Game built with Python and Turtle graphics.

The player controls a snake that grows longer as it eats food while avoiding walls and its own tail. The game includes score tracking, high score saving, save/load functionality, and restart controls.

---

## Purpose of the Software

The purpose of this project was to practice object-oriented programming concepts in Python while building an interactive game.

This project demonstrates:

- Classes and objects
- File handling
- Collision detection
- Keyboard event handling
- Game loops
- Saving and loading data
- Modular programming

---

## Development Environment

- Python 3
- Turtle graphics library
- Visual Studio Code
- GitHub

---

## How to Run the Game

### 1. Install Python

Download Python from:

- https://www.python.org

Make sure Python is added to your system PATH during installation.

---

### 2. Download the Project Files

Make sure all files are in the same folder:

- `main.py`
- `snake.py`
- `food.py`
- `score.py`
- `data.txt`

---

### 3. Run the Game

Open a terminal or command prompt in the project folder and run:

```bash
python main.py
```

---

## Controls

| Key | Action |
|---|---|
| Up Arrow | Move Up |
| Down Arrow | Move Down |
| Left Arrow | Move Left |
| Right Arrow | Move Right |
| S | Save Game |
| L | Load Game |
| R | Restart Game |

---

## Game Rules

- Eat food to grow the snake and increase your score.
- If the snake hits the wall:
  - The game ends
  - A game over screen appears
  - Press `R` to restart
- If the snake hits its own tail:
  - The game ends
  - A game over screen appears
  - Press `R` to restart

---

## High Score System

The game saves the highest score in a file called:

```text
data.txt
```

This allows the high score to persist even after closing the game.

---

## Save and Load Game

The game allows the player to save and load their progress.

### Save Game

Press `S` to save the current game.

The saved game includes:

- Current score
- High score
- Snake position
- Snake direction
- Food position

### Load Game

Press `L` to load the saved game.

The game data is stored in:

```text
savegame.json
```

---

## Code Overview

### `main.py`

Handles:

- Screen setup
- Main game loop
- Keyboard controls
- Collision detection
- Save/load functionality
- Restart functionality

### `snake.py`

Contains the `Snake` class:

- Snake creation
- Snake movement
- Snake growth
- Direction handling
- Snake reset logic

### `food.py`

Contains the `Food` class:

- Random food placement
- Food appearance

### `score.py`

Contains the `Score` class:

- Score tracking
- High score tracking
- Game over display
- Scoreboard updates

---

## Useful Websites

- https://docs.python.org/3/
- https://docs.python.org/3/library/turtle.html
- https://www.w3schools.com/python/

---

## Future Work

Possible upgrades for the project:

- Add difficulty levels
- Add sound effects
- Add colored snake segments
- Add obstacles
- Add a start menu
- Add pause functionality
- Add power-ups
- Add different maps
- Add multiplayer support

---

## Video Demonstration

[Software Demo Video](PASTE_YOUR_YOUTUBE_LINK_HERE)

---

## Author

Created by Christina Lane