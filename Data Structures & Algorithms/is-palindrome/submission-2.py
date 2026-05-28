'''
Brute Force:
1. Iterate through string, adding only alphanumeric chars to a new string --> O(n) time, O(n) space
2. Check if that string is equal to itself reversed --> O(n) time, O(n) space
O(n) time, O(n) space

Two Pointers:
1. Init a left and right pointer
2. If either pointer is at a non-alphanumeric char, skip it
3. Compare values at both pointers, if they are not equal anywhere return false

O(n) time, O(1) space
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True