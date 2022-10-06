class MatrixMListNode:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value 
        self.nextCol = None 
        self.nextRow = None
    

class _SparseMatrixIterator:
    def __init__(self, rowArray):
        self._rowArray=rowArray
        self._curRow = 0
        self._curNode = None
        self._findNextElement()
    
    def __iter__(self):
        return self
