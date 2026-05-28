class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for idx1, num1 in enumerate(numbers, start=1):
            idx2 = 1
            if idx1 == idx2:
                idx2 += 1
            while idx2 <= len(numbers):
                if num1 + numbers[idx2-1] == target:
                    return [min(idx1, idx2), max(idx1, idx2)]
                idx2 += 1
            



'''
1. Set up enumerate, similar to two sum
2. Set a pointer but if it's at the same element as i, 
iterate past since we can't use the same element twice
3. After each iteration with 2nd poiner, set it back equal to first value
4. Check whichever index is less and make it appear first in the answer

idx1 = 1
num1 = 1

idx2 = 2
num2 = 2

'''
        