class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None:
            return 0
        res = 0

        for idx, curr in enumerate(height):
            l, r = 0, len(height) - 1
            lMax, rMax = 0, 0
            while l < idx:
                lMax = max(height[l], lMax)
                l += 1
            while r > idx:
                rMax = max(height[r], rMax)
                r -= 1
            water = min(lMax, rMax) - curr
            if water > 0:
                res += water
        
        return res