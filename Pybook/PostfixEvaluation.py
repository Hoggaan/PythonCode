from Pybook.StackLinkList import Stack
def postfixEval(string):
    A, B, C, D = 2,3,6,3
    for chr in string:
        stack = Stack()
        if chr in (A, B, C, D):
            stack.push(chr)
"""         elif chr in (*,/,+,-) and not stack.isEmpty():
            x = stack.pop()
            y = stack.pop()
            #z = x chr y
            stach.push(z) """
        
