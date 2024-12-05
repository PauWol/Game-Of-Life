# Game of Life Simulation

This is a simple implementation of the Game of Life simulation using Python. The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway.

## Table of Contents

- [Game of Life Simulation](#game-of-life-simulation)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
  - [How it Works](#how-it-works)
  - [Other Aspects](#other-aspects)
  - [Using this Simulation with a User Interface](#using-this-simulation-with-a-user-interface)
  - [Example Code](#example-code)
    - [Unlimited Iterations](#unlimited-iterations)
    - [Limited Iterations](#limited-iterations)
  - [Notes](#notes)

## Usage

To run the simulation, simply execute the `game.py` file. The simulation will run indefinitely until the user stops it.

The simulation can be customized by modifying the parameters at the top of the `game.py` file. The available parameters are:

- **`size`**: The size of the grid (default is 9x9)
- **`tickrate`**: The time between each iteration (default is 1 second)
- **`iterations`**: The number of iterations to run (default is 0, which means to run indefinitely)
- **`debug`**: A boolean flag to enable or disable debugging output (default is False)

## How it Works

The Game of Life simulation works by applying the following rules to each cell in the grid:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The simulation starts with an initial state and then applies the rules to each cell in the grid at each iteration. The state of the grid is then printed to the console.

## Other Aspects

The simulation also includes a number of other features, such as:

- A **`World`** class that represents the grid and provides methods for setting cells to alive or dead, checking if a cell is alive or dead, and getting the current state of the world as a 2D list.
- A **`Game`** class that manages the simulation and provides methods for running the simulation, synchronizing the current state with the world's state, and applying the rules to each cell.
- A **`Plotter`** class that displays the state of the world as a graphical plot. This class is used to display the state of the world when the `debug` parameter is set to True.

## Using this Simulation with a User Interface

If you want to use this simulation with a user interface, you can use the following methods to interact with the simulation:

- **`__init__`**: To initialize the simulation with the desired parameters, such as the grid size and the number of iterations.
- **`updateWorld`**: To set the initial state of the world by providing a 2D list of 0s and 1s, where 0 represents a dead cell and 1 represents a live cell.
- **`tick`**: To run one complete iteration of the simulation. This method will apply the rules of the Game of Life to each cell in the grid and update the state of the world. It also returns the current state of the world as a 2D list.

Note that the user interface should be designed to match the size and iteration settings of the simulation.

## Example Code

### Unlimited Iterations

Below is an example of how to set up and run the Game of Life simulation using the provided classes when intended to build a UI for it:

```python
# Import the Game class from the game module
from game import Game

# Define the initial state of the world as a 2D list
# 0 represents a dead cell, and 1 represents a live cell
initial_state = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Initialize the Game object with desired parameters
game = Game(size=9, tickrate=1, iterations=0)

# Set the initial state of the world
game.updateWorld(initial_state)

while True:
    """
    The tick method applies the rules of the Game of Life to each cell in the grid and updates the state of the world. It also creates a timeout by the tickrate parameter.
    """
    print(game.tick())
```

- The **`size`** parameter defines the dimensions of the grid. In this example, it is set to 9x9.
- The **`tickrate`** parameter controls the time delay between each iteration. It is set to 1 second here.
- The **`iterations`** parameter determines the number of iterations to run the simulation. Setting it to 0 will run indefinitely.
- The **`debug`** parameter is set to `false` to disable debugging mode, which would print the state of the world at each iteration and create a plot.
- The **`initial_state`** is a 2D list representing the starting configuration of the grid. Adjust this to test different patterns.

### Limited Iterations

Below is an example of how to set up and run the Game of Life simulation with a limited number of iterations:

```python
# Import the Game class from the game module
from game import Game

# Define the initial state of the world as a 2D list
initial_state = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Initialize the Game object with desired parameters
game = Game(size=9, tickrate=1, iterations=10)

# Set the initial state of the world
game.updateWorld(initial_state)

for _ in range(game.iterations):
    """
    The tick method applies the rules of the Game of Life to each cell in the grid and updates the state of the world. It also creates a timeout by the tickrate parameter.
    """
    print(game.tick())
```

> In this example, the **`iterations`** parameter is set to 10, meaning the simulation will run for 10 iterations.

## Notes

This implementation of the Game of Life simulation is very basic and does not include any advanced features, such as boundary conditions or a user interface. It is intended as a simple example of how the Game of Life can be implemented in Python.
