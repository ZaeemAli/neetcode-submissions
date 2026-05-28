'''
1. Iterate through each row
    - If target is greater than the last value in the row, skip to next row
        - If target is less than first value of the next row, return false
2. Binary search on the row to find value
    - If value exists return true, otherwise false
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            if target < row[0]:
                return False
            elif target > row[len(row) - 1]:
                continue

            #found row where value should be
            l, r = 0, len(row) - 1
            while l <= r:
                mid = (l + r) // 2
                if target < row[mid]:
                    r = mid - 1
                elif target > row[mid]:
                    l = mid + 1
                else:
                    return True
        return False

