"""
Find captured black items
"""
from collections import deque
from enum import Enum


class Node(Enum):
    BLACK = 5
    WHITE = 2
    EMPTY = 0


class Grid():

    def __init__(self, size, nodepairs):
        super().__init__()

        self.board = [[Node.EMPTY for i in range(size)] for j in range(size)]
        self.size = size
        for node in nodepairs:
            self.setVal(self.board, node[0], node[1])

    def get(self, arr, location):
        return arr[location[0]][location[1]]

    def setVal(self, arr, location, value):

        arr[location[0]][location[1]] = value

    def isCaptured(self, location):
        if (self.get(self.board, location) == Node.WHITE):
            return False
        if self.isntOut(location):
            q = deque()
            q.appendleft(location)
            visited = [[False for i in range(self.size)]
                       for j in range(self.size)]
            self.setVal(visited, location, True)
            while len(q) != 0:
                curr = q.popleft()
                self.setVal(visited, curr, True)
                if self.isSurrounded(q, visited, curr):
                    continue
                else:
                    return False
            return True
        else:
            return False

    def isntOut(self, location):
        if (location[0] >= 0 and location[0] < self.size and location[1] >= 0 and location[1] < self.size):
            return True
        return False

    def isSurrounded(self, q, visited, curr):
        neighbors = [[curr[0], curr[1]+1], [curr[0], curr[1]-1],
                     [curr[0]+1, curr[1]], [curr[0]-1, curr[1]]]
        for loc in neighbors:
            if self.isntOut(loc):
                if not self.get(visited, loc):

                    if self.get(self.board, loc) == Node.WHITE:
                        self.setVal(visited, loc, True)
                        continue
                    elif self.get(self.board, loc) == Node.EMPTY:
                        return False
                    elif self.get(self.board, loc) == Node.BLACK:
                        q.append(loc)
            else:
                continue
        return True


if __name__ == "__main__":
    newGrid = Grid(5, [([1, 3], Node.WHITE),
                       ([1, 2], Node.WHITE),
                       ([3, 3], Node.WHITE),
                       ([3, 2], Node.EMPTY),
                       ([2, 1], Node.WHITE),
                       ([2, 4], Node.WHITE),
                       ([2, 2], Node.BLACK),
                       ([2, 3], Node.BLACK),
                       ])
    print(newGrid.isCaptured([2, 2]))
