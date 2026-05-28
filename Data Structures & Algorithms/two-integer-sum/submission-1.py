'''
1. Create a hashmap/dictionary of elements in list and their index
2. For each element in list, target - element = diff
3. If diff in hashmap, get index from hashmap and other index from for loop
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hmap:
                return [min(hmap[diff], idx), max(hmap[diff], idx)]
            else:
                hmap[num] = idx
        return []
        