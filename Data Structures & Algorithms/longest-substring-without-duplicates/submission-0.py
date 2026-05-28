'''
1. Set up left and right pointers
2. Add letters into hashset since it can't have duplicates
3. Create variable that stores longest length of hashset
4. If you find a letter already in hashset, move left pointer and remove from set

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            res = max(res, r - l + 1)
        return res