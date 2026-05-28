'''
1. Set up left and right pointer
2. Create a variable that stores the max amount of water. Will get updated as we go
3. Check area based on height and width of current pointers
4. Update max amount of water variable and move shorter pointer
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = (r - l) * (min(heights[l], heights[r]))
            if area > res:
                res = area
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1
        return res