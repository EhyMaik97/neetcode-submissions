class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = defaultdict(list)
        for word in strs:
            counter_char = [0] * 26
            for i in word:
                counter_char[ord(i) - ord("a")] += 1
            anagram_hash[tuple(counter_char)].append(word)
        return list(anagram_hash.values())