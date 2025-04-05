class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        from collections import deque

        def isValid(r, c) -> bool:
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        q = deque([(0, 0, 0, k)]) # row, col, steps, breakable blocks
        seen = {(0, 0, k)}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            currRow, currCol, currSteps, currK = q.popleft()

            if currRow == len(grid) - 1 and currCol == len(grid[0]) - 1:
                return currSteps

            for dirRow, dirCol in directions:
                newRow = currRow + dirRow
                newCol = currCol + dirCol

                if isValid(newRow, newCol):
                    # another layer of check for breakable blocks 
                    if grid[newRow][newCol] == 1 and currK > 0 and (newRow, newCol, currK - 1) not in seen: # we break a block
                        q.append((newRow, newCol, currSteps + 1, currK - 1))
                        seen.add((newRow, newCol, currK - 1))
                    elif grid[newRow][newCol] == 0 and (newRow, newCol, currK) not in seen:
                        q.append((newRow, newCol, currSteps + 1, currK))
                        seen.add((newRow, newCol, currK))
            
        return -1

"""
- This is a BFS problem where we keep track of the amount of breaks we have
- Do a standard BFS, in the seen set, we want to ensure that we’re keeping track of the row and column we visited but also the amount of breaks we have at that moment in time, we can visit the same row and column but have a different amount of breaks, one could lead to an optimal solution, another one wouldn’t
- Make sure to do the “seen” checks when you’re checking the two cases when you actually want to append to the queue
- These 2 cases are when you meet with an obstacle and still have breakable blocks left, and the other case is if it's just an empty square
- Keep track of steps taken, blocks broken, and rows and col in the queue
- Return the current steps taken to the end if we reach it, if it isn't reached return a -1 outside of the queue
- Time complexity: O(n) where n is the number of rows x columns in the worst-case
- Space complexity: O(n*k) in case we visit basically all of the rows x columns and exhaust all possible values of breakable blocks, where k is the number of blocks we can break
"""
