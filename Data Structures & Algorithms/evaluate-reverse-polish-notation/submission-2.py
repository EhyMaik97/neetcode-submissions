class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                if token == "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                if token == "*":
                    stack.append(stack.pop() * stack.pop())
                if token == "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(float(b) / a))
        
        return stack[0]

