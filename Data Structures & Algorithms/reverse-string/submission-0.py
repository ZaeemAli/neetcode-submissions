'''
1. Set up left and right pointers
2. Create a temp pointer
3. Assign value at s[l] to temp
4. Set s[l] = s[r] and s[r] = temp
5. Move pointers and repeat steps 3 and 4

Edge cases:
1. Odd number of elements - l and r will be equal, no swapping needed
2. Even number of elements - l > r, so loop will stop
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l,r,temp = 0, len(s) - 1, 0

        while l < r:
            if l == r:
                break
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
        
        return s
        
        