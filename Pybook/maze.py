from array import Array2D
from Pybook.StackLinkList import Stack

class Maize:
    # Define Constants to represent maize contents
    MAIZE_WALL = '*'
    PATH_TOKEN = 'x'
    TRIED_TOKEN = 'o'

    # Create a maize object with all cells marked as open
    def __init__(self, numRows, numCols):
        self._maizeCells = Array2D(numRows, numCols)
        self._startCell = None
        self._exitCell = None

    # Returns the number of rows in the maize
    def numRows(self):
        return self._maizeCells.numRows()
    
    # Returns the number of cols in the maize
    def numCols(self):
        return self._maizeCells.numCols()
    
    # Fills the indicated cell with a "Wall" marker 
    def setWall(self, row, col):
        assert row >= 0 and row <= self.numRows() and \
            col >= 0 and col <= self.numCols(), "Cell Index Out of Range"
        self._maizeCells.set(row, col, self.MAIZE_WALL)

    # Sets the starting positon
    def setStart(self, row, col):
        assert row >= 0 and row <= self.numRows() and \
            col >= 0 and col <= self.numCols(), "Cell Index Out of Range"
        self._startCell._CellPositon(row, col)
    
    # Sets Exit Cell possition
    def setExit(self, row, col):
        assert row >= 0 and row <= self.numRows() and \
            col >= 0 and col <= self.numCols(), "Cell Index Out of Range"
        self._exitCell._CellPositon(row, col)

    # Atempts to find path from the staring position to the end
    # Returns True if the path is found. False otherwise
    def findPath(self):
        pass    
    # Reset the maize
    def reset(self):
        pass

    def draw(self):
        pass
    
    # Returns True if the given cell position is valid move
    def isValid(self, col, row):
        return row>=0 and row < self.numRows() and \
            col >= 0 and col < self.numCols() and \
                self._maizeCells[row, col] is None

    # Helper function if the exit is found
    def _exitFound(self, row, col):
        return row == self._exitCell.row and col == self._exitCell.col 
    
    # Drops a "Tried" token at given cell
    def _markTried(self, row, col):
        self._maizeCells.set(row, col, self.TRIED_TOKEN)
    
    # Drops a path at a given token
    def _markPath(self, row, col):
        self._maizeCells.set(row, col, self._markPath)


class _CellPosition(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
