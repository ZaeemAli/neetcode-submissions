'''
1. Hashmap where key=num, value=# of occurrences
2. Loop through the hashmap k times to find the nums withe the greatest values
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)

        sorted_keys = sorted(hmap, key=hmap.get, reverse=True)
        return sorted_keys[:k]
            
        