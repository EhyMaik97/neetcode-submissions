class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { ")": "(", "]": "[", "}": "{" }
        stack = []

        for i in s: 
            if i not in brackets:
                stack.append(i)
            else:
                if stack and stack[-1] == brackets[i]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0