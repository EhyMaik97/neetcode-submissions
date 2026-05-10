class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            base = r - l
            curr_height = min(heights[l], heights[r])
            curr_area = base * curr_height

            max_water = max(max_water, curr_area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_water