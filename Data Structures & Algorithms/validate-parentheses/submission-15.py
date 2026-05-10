class Solution:
    def isValid(self, s: str) -> bool:
        close_brackets = {"}": "{", ")": "(", "]": "["}
        stack = []

        for i in range(len(s)):
            if s[i] not in close_brackets:
                stack.append(s[i])
            else:
                if not stack or stack.pop() != close_brackets[s[i]]:
                    return False
                    
        return len(stack) == 0