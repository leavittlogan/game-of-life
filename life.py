import random as r

class Life():
    """Class to simulate Conways game of Life"""

    def __init__(self, dimensions, pattern = None):
        self.grid = []
        self.rows, self.cols = dimensions

        if pattern == None:
            r.seed()
            for i in range(self.rows):
                self.grid.append([])
                for j in range(self.cols):
                    self.grid[i].append(r.getrandbits(1) == 0)
        else:
            self.grid = [[False for j in range(self.cols)] for i in range(self.rows)]

            start_row = self.rows//2 - len(pattern)//2
            start_col = self.cols//2 - len(pattern[0])//2
            for i in range(len(pattern)):
                for j in range(len(pattern[i])):
                    self.grid[start_row + i][start_col + j] = pattern[i][j]



    def next_gen(self):
        new_grid = []

        for i in range(self.rows):
            new_grid.append([])
            for j in range(self.cols):
                count = self._neighbour_count(i, j)
                if self.grid[i][j]:
                    new_grid[i].append(count == 2 or count == 3)
                else:
                    new_grid[i].append(count == 3)

        self.grid = new_grid


    def _neighbour_count(self, row, col):
        count = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                count += self.grid[i % self.rows][j % self.cols]

        return count - self.grid[row][col]
