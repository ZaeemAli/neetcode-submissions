'''
1. Set up left and right pointers
4. Set s[l] = s[r] and s[r] = s[l] in one line since python executes line by line
5. Move pointers and repeat steps 3 and 4

Edge cases:
1. Odd number of elements - l and r will be equal, no swapping needed
2. Even number of elements - l > r, so loop will stop
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        return s
        
        