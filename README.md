# PathfinderGame
## Description
This is a simple grid-based adventure game where the player (denoted by 'P') navigates through a grid to reach the target ('T'). The player needs to avoid obstacles (denoted by '#') placed randomly on the board. The objective is to start from the top-left corner (denoted by 'S') and reach the bottom-right corner (denoted by 'T'). The game ends when the player either collides with an obstacle or reaches the target.
## Features
- Grid Board: A customizable grid of size NxN where obstacles are placed randomly.
- Player Movement: The player can move up, down, left, or right.
- Obstacles: Random obstacles are placed on the grid, and the player must avoid them.
- Win Condition: Reach the target 'T' to win the game.
- Collision Detection: Colliding with an obstacle results in a game over.
- Out of Bounds Check: Ensures the player doesn't move out of the grid.

## Requirements
- Python 3.x

## How to Run
**1.** Clone the repository or copy the code to your local machine.

**2.** Open a terminal or command prompt.

**3.** Navigate to the directory containing the script.

**4.** Run the Python script using the following command:
```bash 
python ThePathfinderGame.py
```

## Gameplay
**1.** The game board is displayed as a grid of characters. The starting point ('S') is at the top-left, and the target ('T') is at the bottom-right.

**2.** The player starts at position 'P'. Move the player by entering one of the following directions:
- 'up' to move the player up.
- 'down' to move the player down.
- 'left' to move the player left.
- 'right' to move the player right.
  
**3.** The game will alert the player if they try to move out of bounds or if they collide with an obstacle.
  
**4.** The player wins by reaching the target ('T').

## Code Explanation
**create_board(size, num_of_obstacles)**

Generates a board of size NxN, placing obstacles randomly. The start ('S') is placed at the top-left corner, and the target ('T') is placed at the bottom-right corner. The player's initial position is also marked as 'P'.

**move_player(board, position, direction)**

Handles the player's movement based on the direction input ('up', 'down', 'left', 'right'). It checks for out-of-bound moves, obstacle collisions, and win conditions.

**display_board(board)**

Displays the current state of the board to the player, showing the player’s current position, obstacles, and the target.

## Example
Here is an example of how the board might look in one of the rounds of the game:

![pathfinder game board](https://github.com/user-attachments/assets/9e1df8d3-0938-43b0-8d6a-7cdfc8272220)

### Where:

- 'P' is the player.

- '#' represents an obstacle.

- 'T' is the target.

- '.' represents an empty space.

## Contributing
Feel free to fork the repository, make changes, and submit pull requests. Contributions to improve the game mechanics, add new features, or fix bugs are always welcome!

## License
This project is open-source and available under the MIT License.


