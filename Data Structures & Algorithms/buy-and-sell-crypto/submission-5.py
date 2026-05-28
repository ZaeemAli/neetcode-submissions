'''
1. Set up left and right pointer. Left = 0, right = len(prices) - 1
2. While r is in range, if r > l, store profit
3. If l > r, move l = r and increment r by one
O(n) time
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            l, r = 0, 1
            res = 0

            while r < len(prices):
                if prices[l] < prices[r]:
                    profit = prices[r] - prices[l]
                    res = max(res, profit)
                else:
                    l = r
                r += 1
            
            return res
                
        