from pythonds3 import Queue


class ExpressionTree:
    # Builds an expresion tree for the expression string
    def __init__(self, expStr):
        self._expTree = None
        self._buildTree(expStr)

    # Evaluates the expression Tree and returns the resulting Node
    def evaluate(self,varMap):
        return self.evalTree(self._expTree, varMap)
    
    # return a string representaion of the expression tree
    def __str__(self):
        return self._buildString(self._expTree)
    
    # Recursively build a string representation of the expresion Tree
    def _BuildString(self, treeNode):
        # If the node is a leaf, it is an operand
        if treeNode.left is None and treeNode.right is None:
            return str(treeNode.element)
        else: # Otherwise it is an operator
            expStr = '(' 
            expStr += self._BuildString(treeNode.left)
            expStr += treeNode.element
            expStr += self._BuildString(treeNode.right)
            expStr += ')'
            return expStr

    def _evalTree(self, subTree, varDict):
        # See if the node is a leaf node, in which case return its value.
        if subTree.left is None and subTree.right is None:
            # Is the operand the literal digit
            if subTree.element >= '0' and subTree.element <= '9':
                return int(subTree.element)
            else:
                assert subTree.element in varDict, "Invalid Variable!"
                return varDict[subTree.element]
        else:
            lvalue = self._evalTree(subTree.left, varDict)
            rvalue = self._evalTree(subTree.right, varDict)
            return computeOp(lvalue, subTree.element, rvalue)
    
    # Compute the arithmeitc operation based on the supplied op string
    def _computeOp(left, op, right):
        pass

    def _buildTree(self, expStr):
        # Build the Queue containing the tokens in the expression String
        expQ = Queue()
        for token in expStr:
            expQ.enqueue(token)
        # Create an empty root node
        self._expTree = _ExpTreeNode(None)
        # Call the recursive function to the recursive Tree
        self._recBuildTree(self._expTree, expQ)
    
    # Recursively build the tree given an intial root node
    def _recBuildTree(self, curNode, expQ):
        token = expQ.dequeue()
        # Check if the token is '('
        if token == '(':
            curNode.left = _ExpTreeNode(None)
            self._recBuildTree(curNode.left, expQ)
        
        curNode.data = expQ.dequeue()
        curNode.right = _ExpTreeNode(None)
        self._recBuildTree(curNode.right, expQ)

        # the next token ')' will be removed
        expQ.dequeue()

        # else:
        #     curNode.element = token

        

    

    
# class for creating the Tree Nodes
class _ExpTreeNode:
    def __init__(self, data):
        self.element = data
        self.right = None
        self.left = None
    

