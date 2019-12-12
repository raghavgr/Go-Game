import unittest
from capturedGrid import Grid
from capturedGrid import Node


class TestGridGo(unittest.TestCase):

    """
    Initializing a board with the following setup:
    EEWWEE
    EWBBWE
    EEWWEE
    """

    def setUp(self):
        self.location = [2, 2]
        self.grid = Grid(5, [([1, 3], Node.WHITE),
                             ([1, 2], Node.WHITE),
                             ([3, 3], Node.WHITE),
                             ([3, 2], Node.WHITE),
                             ([2, 1], Node.WHITE),
                             ([2, 4], Node.WHITE),
                             ([2, 2], Node.BLACK),
                             ([2, 3], Node.BLACK),
                             ])
        return super().setUp()

    """
    Check that the node at the [2, 2] is BLACK
    """

    def test_get(self):
        curr = self.grid.get(self.grid.board, self.location)
        self.assertEqual(Node.BLACK, curr)

    """
    Set the value at [2, 2] as EMPTY and
    check that it is true
    """

    def test_setVal(self):
        self.grid.setVal(self.grid.board, self.location, Node.EMPTY)
        curr = self.grid.get(self.grid.board, self.location)
        self.assertEqual(Node.EMPTY, curr)

    """
    Check that the node is not captured at the location
    """

    def test_isCaptured(self):
        self.assertEqual(True, self.grid.isCaptured(self.location))

    """
    Use [2, 1] location of white node to test isCaptured
    """

    def test_isNotCaptured(self):
        self.assertEqual(False, self.grid.isCaptured([2, 1]))

    """
    Set [3, 2] to be empty to fail isSurrounded function
    """

    def test_isNotSurrounded(self):
        self.grid.setVal(self.grid.board, [3, 2], Node.EMPTY)
        self.assertEqual(False, self.grid.isCaptured([3, 2]))


if __name__ == "__main__":
    unittest.main()
