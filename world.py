"""
Module containing World class for representing a Game of Life world.

This module contains the World class which is used to represent a Game of Life
world. The World class has methods for setting cells to alive or dead, checking
if a cell is alive or dead, and getting the current state of the world as a 2D
list.

"""

class World:
    def __init__(self,size:int = 9):
        """
        Initialize World object with given size.

        :param size: size of the world
        :type size: int
        """
        self._size: int = size
        self._yxui: list[list[int]] = [[0 for _ in range(size)] for _ in range(size)]
    
    def is_alive(self,y:int,x:int):
        """
        Check if cell at given coordinates is alive.

        :param y: y-coordinate of cell
        :type y: int
        :param x: x-coordinate of cell
        :type x: int
        :return: True if cell is alive, False otherwise
        :rtype: bool
        """
        return bool(self._yxui[y][x])
    
    def set_alive(self,y:int,x:int):
        """
        Set cell at given coordinates to alive.

        :param y: y-coordinate of cell
        :type y: int
        :param x: x-coordinate of cell
        :type x: int
        """
        self._yxui[y][x] = 1
        
    def set_dead(self,y:int,x:int):
        """
        Set cell at given coordinates to dead.

        :param y: y-coordinate of cell
        :type y: int
        :param x: x-coordinate of cell
        :type x: int
        """
        self._yxui[y][x] = 0
    
    def clearAll(self):
        """
        Clear all cells in the world.
        """
        for y in range(self._size):
            for x in range(self._size):
                self._yxui[y][x] = 0
    
    @property
    def size(self):
        """
        Get the size of the world.

        :return: size of the world
        :rtype: int
        """
        return self._size
    
    @size.setter
    def size(self,size:int):
        """
        Set the size of the world.

        :param size: new size of the world
        :type size: int
        """
        self._size = size
        self._yxui = [[0 for _ in range(size)] for _ in range(size)]
        
    @property
    def yxui(self):
        """
        Get the current state of the world as a 2D list.

        :return: 2D list representing the current state of the world
        :rtype: list[list[int]]
        """
        return self._yxui
    
    @yxui.setter
    def yxui(self,yxui:list[list[int]]):
        """
        Set the current state of the world from a 2D list.

        :param yxui: 2D list representing the new state of the world
        :type yxui: list[list[int]]
        """
        self._yxui = yxui
    

if __name__ == '__main__':
    world = World(9)
    c = 0
    for y in range(8):
        for x in range(8):
            if c == 2:
                world.set_alive(y,x)
                c = 0
            else:
                c += 1
    print(world.yxui)

    print("\n\n\n")
    
    for y in range(8):
        for x in range(8):
            print(world.is_alive(y,x))