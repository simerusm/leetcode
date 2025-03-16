# Better Solution

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

"""
- Binary search problem
- Treat the entire 2D array as one array with indices [0, m * n - 1], squash it essentially
- Same binary search procedure of left and right pointer with one twist, we need to determine which index from [0, m * n - 1] corresponds to which element in the 2D array
- To find row:
    - Each row contains indexes [0, n-1], [n, 2*n-1], ..., thus when given an index from [0, m * n - 1], i // n where n is the length of a row (# of cols) will get you the row index
- To find col:
    - After every column index, the next time the same index occurs is exactly n away
    - E.g. Index 0 belongs to the 0th column, and then every n indices we are back in the 0th column. Index 1 belongs to the 1st column, and then every n indices we are back in the 1st column. 
    - Because each column is spaced by n indices, the modulus operator gives us the column.
    - So to find col we do i % n
- Use the row and col calculated after getting the index to proceed with regular binary search
- Time Complexity: O(log(n*m)), we're doing a binary search on the 2D array as if it were squashed which has a length of n*m where n and m are the number of rows and columns
- Space Complexity: O(1)
"""


# Ok Solution

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lRow = 0
        lCol = 0

        rRow = len(matrix) - 1
        rCol = len(matrix[rRow]) - 1

        while lRow <= rRow and lCol <= rCol:
            mRow = (lRow + rRow) // 2
            mCol = (lCol + rCol) // 2
            currVal = matrix[mRow][mCol]

            if currVal == target:
                return True
            
            # we only adjust the column pointers when we're locked in on the row
            # if we're on the right row
            if (matrix[mRow][lCol] <= target and target <= matrix[mRow][rCol]):
                # don't make any changes to lRow and rRow, mRow will stay the same
                # just need to change the col values
                if currVal > target:
                    rCol = mCol - 1
                elif currVal < target:
                    lCol = mCol + 1

            # the row is not the right row, we need to move down
            elif currVal > target and not (matrix[mRow][lCol] < target and target < matrix[mRow][rCol]):
                rRow = mRow - 1
            # row is not right row, need to move up
            elif currVal < target and not (matrix[mRow][lCol] < target and target < matrix[mRow][rCol]):
                lRow = mRow + 1

        return False
