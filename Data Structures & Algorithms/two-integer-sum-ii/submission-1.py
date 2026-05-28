class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        while l != r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                break
        return [l+1, r+1]

'''
1. Set up two pointers
2. If sum is greater than target, shift right pointer to the left
3. If sum is less than target, shift left pointer to the right

'''
        