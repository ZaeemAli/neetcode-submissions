'''
1. Hashset can't have duplicates
2. Iterate through list adding to hashmap
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for num in nums:
            if num in hset:
                return True
            else:
                hset.add(num)
        return False