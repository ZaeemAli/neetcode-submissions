'''
1. Sliding window approach
2. Set up both pointers at index 0
3. Move one pointer over and store price[r] - price[l] as answer
4. Iterate through and update answer if greater than previous value
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer, l, r = 0, 0, 0

        while l < len(prices) - 1:
            while r < len(prices) - 1:
                r += 1
                if prices[r] - prices[l] > answer:
                    answer = prices[r] - prices[l]
            l += 1
            r = l
        
        return answer
            
        