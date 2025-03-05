class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        from collections import deque

        def isExit(r, c) -> bool:
            return r == 0 or r == len(maze) - 1 or c == 0 or c == len(maze[0]) - 1
        
        def isValid(r, c) -> bool:
            return 0 <= r < len(maze) and 0 <= c < len(maze[0]) and (r, c) not in seen and maze[r][c] != "+"

        res = float('inf')
        q = deque([(entrance[0], entrance[1], 0)])
        seen = {(entrance[0], entrance[1])}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            currRow, currCol, currSteps = q.popleft()

            if isExit(currRow, currCol) and currSteps != 0:
                res = min(res, currSteps)
            
            for dirRow, dirCol in directions:
                if isValid(currRow + dirRow, currCol + dirCol):
                    q.append((currRow + dirRow, currCol + dirCol, currSteps + 1))
                    seen.add((currRow + dirRow, currCol + dirCol))
        
        if res == float('inf'):
            return -1
        return res

"""
- This is just a BFS problem with us storing steps in each BFS node/state
- Do a BFS starting from the entrance node
  - Have a directions array containing all directions you can go in from a given node
- In the queue for the BFS, keep track of the row, column, and steps taken to get to that place
- Have two functions to validate moves and check if we’re at an entrance
  - IsExit function should check if we’re at an outer layer of the matrix
  - isValid function should check if the current move is valid by checking if it’s in bounds, if it hasn’t been seen yet, and if it’s not a “+”
- In the BFS while loop pop the front from the queue and then check if it's on an exit row/column and if it is update the result variable if it is a minimum
- Loop through all possible directions you could go to starting from the node you popped off from the queue by checking if it's valid and then if it is add it to the queue and seen set
- At the end, if the result variable is still infinity return a -1 indicating we couldn’t reach it, otherwise just the result itself
- Time complexity: O(m x n) where m is the number of rows and n is the number of columns since at most each cell could be visited once; the queue and check operations are all constant time
- Space Complexity: O(m x n) at most since we can visit all cells at most once and add them to the visited set
"""
