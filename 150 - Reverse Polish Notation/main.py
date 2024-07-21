class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for char in tokens:
            if char == "+" or char == "-" or char == "/" or char == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                res = calculate(num1, num2, char)
                stack.append(res)
            else:
                stack.append(int(char))
                
        return stack.pop()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a/b

def multiply(a, b):
    return a * b

operations = {
        "+": add,
        "-": subtract,
        "/": divide,
        "*": multiply,
        }

def calculate(a, b, symbol):
    return operations[symbol](a, b)
