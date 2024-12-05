"""
Module containing Game class for running a game of life simulation.

This module contains the Game class which is used to run a game of life
simulation. The Game class has methods for setting cells to alive or dead,
checking if a cell is alive or dead, and getting the current state of the
world as a 2D list.

"""
from world import World
from visualize import Plotter
from time import sleep

class Game:
    def __init__(self,size:int = 9,tickrate:int = 1,iterations:int = 0,debug:bool = False):
        """
        Initialize Game object with given size, tickrate, iterations, and debug status.

        :param size: size of the world
        :type size: int
        :param tickrate: time between each iteration
        :type tickrate: int
        :param iterations: number of iterations to run
        :type iterations: int
        :param debug: if True, print the state of the world at each iteration
        :type debug: bool
        """

        self.size = size
        self.tickrate = tickrate
        self.iterations = iterations
        self.i = 0
        self.debug = debug
        
        
        self.yxnow: list[list[int]] = [[0 for _ in range(size)] for _ in range(size)]
        self.yxfuture: list[list[int]] = [[0 for _ in range(size)] for _ in range(size)]
        self.world = World(size)
    
        if debug: self.plotter = Plotter(self.world.yxui)
    
    def debuger(self):
        """
        If debug is True, print the current state of the world and update the plotter.

        :return: None
        """
        if self.debug:
            print(self.world.yxui)
            self.plotter.update(self.world.yxui)
        
    def syncroniseYxnow(self):
        """
        Synchronise the yxnow list with the state of the world.
        
        :return: None
        """
        for y in range(self.size-1):
            for x in range(self.size-1):
                if self.world.is_alive(x,y):
                    self.yxnow[y][x] = 1
                else:
                    self.yxnow[y][x] = 0
    
    def countNeighbors(self,y:int,x:int):
        """
        Count the number of alive cells neighboring the cell at (x,y) and return the count.

        :param y: y-coordinate of the cell
        :type y: int
        :param x: x-coordinate of the cell
        :type x: int
        :return: number of alive neighbors
        :rtype: int
        """
        count = 0
        if self.yxnow[y][x-1] == 1:
            count = count+1
        if self.yxnow[y][x+1] == 1:
            count = count+1
        if self.yxnow[y-1][x] == 1:
            count = count+1
        if self.yxnow[y-1][x+1] == 1:
            count = count+1
        if self.yxnow[y-1][x-1] == 1:
            count = count+1
        if self.yxnow[y+1][x] == 1:
            count = count+1
        if self.yxnow[y+1][x+1] == 1:
            count = count+1
        if self.yxnow[y+1][x-1] == 1:
            count = count+1
        return count

    def applyRules(self):
        """
        Apply the rules of the Game of Life to each cell in the current state.

        For each cell in the 8x8 grid, this method counts the number of alive neighbors.
        It then applies the appropriate rules based on the current state of the cell:
        - If the cell is alive, it applies rules 1, 2, and 3.
        - If the cell is dead, it applies rule 4.
        
        The results are stored in the future state list, `yxfuture`.
        
        :return: None
        """
        for y in range(self.size-1):
            for x in range(self.size-1):
                n = self.countNeighbors(y,x)
                if self.yxnow[y][x] == 1:
                    self.rule1(n,y,x)
                    self.rule2(n,y,x)
                    self.rule3(n,y,x)
                #for no leaf slots
                if self.yxnow[y][x] == 0:
                    self.rule4(n,y,x)
                
    def rule3(self,n:int,y:int,x:int):
        """
        rule3: If a cell is alive and has two or three alive neighbors, it stays alive in the future state.
        
        :param n: number of alive neighbors
        :type n: int
        :param y: y-coordinate of the cell
        :type y: int
        :param x: x-coordinate of the cell
        :type x: int
        :return: None
        """
        if n == 2 or n == 3:
            self.yxfuture[y][x] = 1
            
    def rule4(self,n:int,y:int,x:int):
        """
        rule4: For a space that is empty or unpopulated, each cell with three alive neighbors becomes populated in the future state.
        
        :param n: number of alive neighbors
        :type n: int
        :param y: y-coordinate of the cell
        :type y: int
        :param x: x-coordinate of the cell
        :type x: int
        :return: None
        """
        
        if n == 3:
            self.yxfuture[y][x] = 1

    def rule2(self,n:int,y:int,x:int):
        """
        rule2: Each cell with four or more alive neighbors dies, as if by overpopulation.
        
        :param n: number of alive neighbors
        :type n: int
        :param y: y-coordinate of the cell
        :type y: int
        :param x: x-coordinate of the cell
        :type x: int
        :return: None
        """
        
        if n >= 4:
            self.yxfuture[y][x] = 0
            
    def rule1(self,n:int,y:int,x:int):
        """
        rule1: Each cell with one or no alive neighbors dies, as if by solitude.
        
        :param n: number of alive neighbors
        :type n: int
        :param y: y-coordinate of the cell
        :type y: int
        :param x: x-coordinate of the cell
        :type x: int
        :return: None
        """
        
        if n == 0 or n == 1:
            self.yxfuture[y][x] = 0
        
    def takeEffect(self):
        """
        Apply the future state to the world by clearing all cells and then setting cells to alive based on the `yxfuture` list.
        """        
        self.world.clearAll()
        for y in range(self.size-1):
            for x in range(self.size-1):
                if self.yxfuture[y][x] == 1:
                    self.world.set_alive(x,y)
    
    @property
    def loopCondition(self):
        """
        Condition to determine if the game should loop again.
        If iterations is set to 0, this condition will always return True.
        Otherwise, it will return True if the current iteration count is less than the iterations parameter.
        """
        if self.iterations == 0:
            return True
        self.i += 1
        return self.i < self.iterations

    def updateWorld(self, inpList: list[list[int]]):
        """
        Update the world state to match the given 2D list, which represents the current state of the world.
        
        :param inpList: 2D list of 0s and 1s representing the current state of the world
        :type inpList: list[list[int]]
        :return: None
        """
        self.world.yxui = inpList

    def tick(self):
        """
        Advance the game state by one iteration.
        
        This method synchronizes the current state with the world's state, applies the 
        rules of the Game of Life to each cell, updates the world with the future state, 
        and outputs the current state if debugging is enabled. The game state progresses 
        at the rate defined by the tickrate.
        
        :return: The current state of the world as a 2D list
        :rtype: list[list[int]]
        """
        self.syncroniseYxnow()
        self.applyRules()
        self.takeEffect()
        self.debuger()
        sleep(self.tickrate)
        return self.world.yxui
    
    def run(self):
        """
        Run the Game of Life simulation.

        Continuously runs the game loop while the looping condition is met.
        During each loop iteration, the current state is synchronized, the rules
        are applied to each cell, the future state is set as the current state, and
        the state of the world is optionally printed and displayed if debugging is enabled.

        The loop runs at a rate determined by the tickrate parameter.

        :return: None
        """
        while self.loopCondition:
            self.tick()

if __name__ == "__main__":
    """
    game = Game(size=10,tickrate=1,iterations=6,debug=True)
    game.world.set_alive(4,6)
    game.world.set_alive(4,5)
    game.world.set_alive(5,4)
    game.world.set_alive(2,5)
    game.world.set_alive(5,6)
    game.run()
    """
    patternList = [[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,1,0,0,0,0,0],
                   [0,0,0,1,0,0,0,0,0],
                   [0,0,0,1,0,0,0,0,0],
                   [0,0,0,1,0,1,1,0,0],
                   [0,0,0,0,0,0,1,0,0],
                   [0,0,0,0,0,0,1,0,0],
                   [0,0,0,0,0,1,0,0,0]]
    
    game = Game(size=9,tickrate=1,iterations=0,debug=True)
    game.updateWorld(patternList)
    game.run()
    