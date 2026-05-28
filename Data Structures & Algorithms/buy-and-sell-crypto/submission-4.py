'''
1. Sliding window approach
2. Set up both pointers at index 0
3. Move one pointer over and store price[r] - price[l] as answer
4. Iterate through and update answer if greater than previous value
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
            
        