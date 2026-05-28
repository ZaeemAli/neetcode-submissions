'''
1. Set up left and right pointer, left=0, right=1
2. Create a list, since it keeps order and add first letter
3. For each new letter
    - If it isn't already in the list, add it
    - If it is, keep popping the first element out until the would-be duplicate is gone, then add the letter
4. Check if the length of the list is greater than the res and update it if so
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 1
        sub = [s[l]]
        res = 1

        while r < len(s):
            if s[r] not in sub:
                sub.append(s[r])
            else:
                while s[r] in sub:
                    sub.pop(0)
                sub.append(s[r])
            if len(sub) > res:
                    res = len(sub)
            r += 1
        
        return res