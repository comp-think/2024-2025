# Workshop - Computational Thinking and Programming 24/25

## Useful documents

**Slides:** [PDF](https://comp-think.github.io/2024-2025/workshop/workshop2425-slides.pdf)

**Main Python file:** [run.py](https://comp-think.github.io/2024-2025/workshop/run.py)

**Group file:** [group.py](https://comp-think.github.io/2024-2025/workshop/group.py)

## Plot

**What happened in the previous episodes:** Myntrakor, also known as Who Must Not Be Thought, created the Tower Labyrinth, a complex system made of 100 squared mazes of different dimensions placed one upon the other designed to custody the Book of Indefinite Pages, containing all the possible books ever written in just one portable volume. Myntrakor hired Urg, a despicable man, as a guarantor of the Tower Labyrinth. Urg implemented a mechanism that allows the walls to move while someone is trying to reach the exit, making it impossible for thieves to enter the Tower Labyrinth, steal the Book of Indefinite Pages, and go out from all the mazes alive.

However, the Interplanetary Guild of Thieves created a special cannon that can be quickly teleported into a maze and can destroy the walls of each maze of the Tower Labyrinth. The problem is that the cannon appears in different positions in each maze, and a thief, to be used to exit the maze, must destroy as many walls as possible with one shoot before moving to the next maze using the free corridor created by the shooting. Can the Interplanetary Guild of Thieves steal the Book of Indefinite Pages and crash all the mazes of the Tower Labyrinth, finally collapsing the entire evil structure created by Myntrakor?

## Rules

1. Each room is a square which is initially filled with an arbitrary number of free cells and walls
1. The thief controls the cannon, initially positioned in a precise cell
1. The thief has just one shot of the cannon to use per room that should be in one of the eight possible direction (up, down, left, right, and the four diagonals)
1. The cannon cannot move in another cell, and its bullet destroy everything is the trajectory between the cannon and the borders of the maze
1. The thief can escape if, with a cannon shot, (s)he can to destroy the maximum number of walls considering the position in which the cannon has been placed
1. The thief cannot cheat – and (s)he is caught to cheat if: 
   * (s)he claims that all possible trajectories for the cannon shooting do not contain any wall
   * (s)he claims to have destroyed a wall that did not exist in the maze

## Function to implement
```
def do_move(maze, cannon)
```

It takes in input:
* `maze`, a list of lists of dictionaries representing the rows of the maze and the cells in each row
* `cannon`, a tuple of X/Y coordinates identifying the current position of the cannon

It returns a list of tuples of two items, where each tuple defines the X/Y coordinates of the walls that have been destroyed shooting with the cannon – e.g. `[(2,1), (3,2), (4,3)]`

Example of a list of lists of dictionaries representing the board:
```
[									# The main list defining the maze
	[								# The first row (i.e. a list) of the maze 
		{	'x': 0,					# X coordinate of the first cell of the first row 
			'y': 0,					# Y coordinate of the first cell of the first row
			'type': 'free' },		# type of cell (‘free’ or ‘wall’) 
		{	'x': 1,					# X coordinate of the second cell of the first row 
			'y': 0,					# Y coordinate of the second cell of the first row
			'type': 'wall' }, ...	# type of cell (‘free’ or ‘wall’) 
	], 
	[ ... ], ...					# The second row (i.e. a list) of the maze 
]
```

To test the implementation of `do_move`, run:

```
python run.py
```