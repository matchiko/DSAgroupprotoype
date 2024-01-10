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
    return char in {'+', '-', '*', '/'}

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    return 0

def infix_to_postfix(infix_expression):
    stack = Stack()
    postfix = []
    
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
            while not stack.is_empty() and precedence(stack.peek()) >= precedence(char):
                postfix.append(stack.pop())
            stack.push(char)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return ''.join(postfix)

# Example usage
infix_expression = "a+b*c-(d/e+f*g)"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)