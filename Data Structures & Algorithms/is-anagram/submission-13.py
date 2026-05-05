class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_char = {}

        for c in s:
            count_char[c] = count_char.get(c, 0) + 1

        for c in t:
            if c not in count_char:
                return False
            count_char[c] -= 1

        for value in count_char.values():
            if value != 0:
                return False

        return True