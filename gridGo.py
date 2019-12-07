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

        # This was the error
        #self.board = [[Node.EMPTY] * size] * size
        self.board = [[Node.EMPTY for i in range(size)] for j in range(size)]
        self.size = size
        for node in nodepairs:
            self.board[node[0][0]][node[0][1]] = node[1]

    def isCaptured(self, location):
        if self.isntOut(location):
            q = deque()
            q.appendleft(location)

            # This was also the error
            #visited = [[False] * self.size] * self.size
            visited = [[False for i in range(self.size)]
                       for j in range(self.size)]

            visited[location[0]][location[1]] = True
            while len(q) != 0:
                curr = q.popleft()
                visited[curr[0]][curr[1]] = True
                neighbors = [[curr[0], curr[1]+1], [curr[0], curr[1]-1],
                             [curr[0]+1, curr[1]], [curr[0]-1, curr[1]]]
                for i in neighbors:
                    if self.isntOut(i):
                        if not visited[i[0]][i[1]]:
                            if self.board[i[0]][i[1]] == Node.WHITE:
                                visited[i[0]][i[1]] = True
                                continue
                            elif self.board[i[0]][i[1]] == Node.EMPTY:
                                return False
                            elif self.board[i[0]][i[1]] == Node.BLACK:
                                q.append(i)
                    else:
                        continue
            return True
        else:
            return False

    def isntOut(self, location):
        if (location[0] >= 0 and location[0] < self.size and location[1] >= 0 and location[1] < self.size):
            # print(str(location) + " isn't out ")
            return True
        return False


if __name__ == "__main__":
    newGrid = Grid(5, [([1, 3], Node.WHITE),
                       ([1, 2], Node.WHITE),
                       ([3, 3], Node.WHITE),
                       ([3, 2], Node.WHITE),
                       ([2, 1], Node.WHITE),
                       ([2, 4], Node.WHITE),
                       ([2, 2], Node.BLACK),
                       ([2, 3], Node.BLACK),
                       ])
    print(newGrid.isCaptured([2, 2]))
