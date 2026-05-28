class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1

        while l < len(prices) - 1:
            while r < len(prices):
                profit = prices[r] - prices[l]
                res = max(res, profit)
                r += 1
            l += 1
            r = l + 1
        return res