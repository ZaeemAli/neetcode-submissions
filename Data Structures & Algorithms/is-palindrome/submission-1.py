'''
1. Set two pointers up, one left and one right
2. Check if chars are alphanum
3. If are, then compare otherwise move pointer that isn't alphanum by 1
4. If at any point the pointers are not equal, return false. Otherwise return true
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l].isalnum():
                if s[r].isalnum():
                    if s[l].lower() != s[r].lower():
                        return False
                    else:
                        l+=1
                        r-=1
                else:
                    r-=1
            else:
                l+=1
        return True

            