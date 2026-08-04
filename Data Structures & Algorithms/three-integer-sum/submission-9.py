class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            left = k + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + nums[k]
                if total == 0:
                    res.append([nums[left], nums[right], nums[k]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        
        return res