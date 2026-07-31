class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_int = defaultdict(int)
        for num in nums:
            counter_int[num] += 1

        arr = []
        for num, cnt in counter_int.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res