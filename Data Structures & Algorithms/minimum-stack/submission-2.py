class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        element = self.stack.pop()
        return element

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return sorted(self.stack)[0]
