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

## Final results
All the functions implemented by each group (that submitted a syntactical-correct Python code - i.e. "It runs, it runs!") were used to run the main Python script [*Cannon Escape*](https://comp-think.github.io/2024-2025/workshop/00_run_cannon_escape.py) with all the groups' implementation. It used [100 different labyrinths](https://github.com/comp-think/2024-2025/tree/main/docs/workshop/rooms) that have been generated randomly running [create_rooms.py](https://comp-think.github.io/2024-2025/workshop/support/create_rooms.py).

The [final results](https://comp-think.github.io/2024-2025/workshop/00_results.txt) of this execution are summarised as follows:

* Groups that avoided cheating: east_coast
* Groups that won at least 30 mazes: members_of_the_brigata, east_coast, team_team, global_variables, garden_babes, everybodys_welcome
* Grouops that won at least 90 mazes: east_coast
* Groups that had the best rank: programmers_al_dente

Concluding:
* *east_coast* members receive 3 points
* *members_of_the_brigata*, *team_team*, *global_variables*, *garden_babes*, *everybodys_welcome*, *programmers_al_dente* members receive 1 point

In case one group want to test its code with the code used for the evaluation (i.e. [`00_run_cannon_escape.py`](https://comp-think.github.io/2024-2025/workshop/00_run_cannon_escape.py)), it is necessary:

* to clone the current directory dedicated to the workshop;
* to copy the file containing the group code in the same directory of `00_run_cannon_escape.py`;
* to import the group file as usual (i.e. `import <group_file_name_without_extension>`);
* to substitute `john_doe` with the name of the imported file in the list `all_players`;
* to run the code with `python 00_run_cannon_escape.py`.

In case it is needed, the file [`john_doe.py`](https://comp-think.github.io/2024-2025/workshop/john_doe.py) provides a possible implementation of the thief.