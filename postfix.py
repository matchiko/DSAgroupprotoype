class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped = self.top.data
            self.top = self.top.next
            return popped
        else:
            return None

    def peek(self):
        return self.top.data if self.top else None

def is_operator(char):
    return char in {'+', '-', '*', '/', '^'}

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    return 0

def infix_to_postfix(infix_expression):
    stack = Stack()
    postfix = []
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    for char in infix_expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() != '(' and not stack.is_empty():
                postfix.append(stack.pop())
            stack.pop()  # Pop '(' from the stack
        elif is_operator(char):
            while not stack.is_empty() and operators.get(stack.peek(), 0) >= operators[char]:
                postfix.append(stack.pop())
            stack.push(char)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return ''.join(postfix)
