import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # go through nums and count occurrences. key = num and value = # of occurrences
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # init empty min heap
        heap = []
        # while the heap has less elements than k, add (value, key) to heap. if more than k elements, pop lowest freq
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        # create result array and append only the num from the heap

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res