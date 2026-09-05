class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset = set()
        l , r = 0, 0
        curr, longest = 0, 0

        while r < len(s):
            while s[r] in hset:
                hset.remove(s[l])
                l += 1
            hset.add(s[r])
            curr = len(hset)
            longest = max(curr, longest)
            r += 1

        return longest