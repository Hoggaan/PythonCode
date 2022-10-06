def solveNQueens(board,col):
    # A solution was found if n-queens have been placed on the board
    if board.numQueens() == board.size():
        return True
    else:
        for row in range(board.size()):
            if board.unguarded(row,col):
                # Place a queen in that square
                board.PlaceQueen(row,col)
                # Continue placing queens in the following columns
                if board.solveQueens(board, col+1):
                    # We are finished if the solution was found
                    return True
                else:
                    # No solution was found with the queen placed in this square, so it 
                    # has to be removed from the board
                    board.removeQueen(row, col)
    # If the loop terminates, no queen can be placed with in this column
    return False
    