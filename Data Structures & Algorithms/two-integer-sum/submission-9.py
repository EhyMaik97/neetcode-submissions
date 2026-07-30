class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i, n in enumerate(nums):
            if target - n in prev_map:
                return [prev_map[target - n], i]
            prev_map[n] = i
