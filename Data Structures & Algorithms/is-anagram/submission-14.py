class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_hash = {}

        for i in range(len(s)):
            counter_hash[s[i]] = counter_hash.get(s[i], 0) + 1
        
        for i in range(len(t)):
            counter_hash[t[i]] = counter_hash.get(t[i], 0) - 1
        
        for val in counter_hash.values():
            if val != 0:
                return False
        return True
        