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
