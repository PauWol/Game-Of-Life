import matplotlib.pyplot as plt
import sys

class Plotter():
    def __init__(self,map:list[list[int]]):
        self.fig, self.ax = plt.subplots()
        self.table = self.ax.table(cellText=map, loc="center")
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        plt.ion()
        plt.draw()
        self.fig.canvas.mpl_connect('close_event', self.on_close)

    def on_close(self, event:object):
        print('Closing plot...')
        sys.exit()
    
    def update(self,map:list[list[int]]):
        self.ax.clear()
        self.table = self.ax.table(cellText=map, loc="center")
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        plt.draw()
        plt.pause(0.1)


if __name__ == '__main__':
    import time
        
    # Define the 2D list
    my_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 1, 0, 0, 0, 0], 
            [0, 0, 0, 1, 1, 1, 0, 0, 0], 
            [0, 0, 1, 1, 1, 1, 1, 0, 0], 
            [0, 0, 0, 1, 1, 1, 0, 0, 0], 
            [0, 0, 0, 0, 1, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]


    p = Plotter(my_list)
    while True:
        my_list[0][0] = 0
        p.update(my_list)
        time.sleep(1)
        my_list[0][0] = 1
        p.update(my_list)
        time.sleep(1)